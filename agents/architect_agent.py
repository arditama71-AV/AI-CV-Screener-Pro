import json
import io
import os
import streamlit as st
from pypdf import PdfReader
from google import genai
from google.genai import types
from utils.logger import get_logger

logger = get_logger("architect_agent")

def extract_text_from_pdf(pdf_file) -> str:
    """Extract full text from a PDF file object using pypdf."""
    try:
        if hasattr(pdf_file, "read"):
            reader = PdfReader(io.BytesIO(pdf_file.read()))
        else:
            reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        logger.info(f"PDF_AGENT: Extracted {len(text)} chars from PDF.")
        return text.strip()
    except Exception as e:
        logger.error(f"PDF_AGENT: Failed to extract PDF text: {e}")
        return ""

def evaluate_resume_with_ai(
    resume_text: str,
    job_description: str,
    candidate_name: str = "Candidate"
) -> dict:
    """
    Call Google Gemini API to evaluate resume against JD.
    Returns dict: {score: int, analysis: str, skills_matched: list, recommendation: str}
    """
    if not resume_text:
        logger.warning(f"AI_AGENT: Empty resume text for '{candidate_name}'. Skipping evaluation.")
        return {"score": 0, "analysis": "Could not extract text from resume.", "skills_matched": [], "recommendation": "Review Manually"}

    try:
        logger.info(f"AI_AGENT: Evaluating resume for '{candidate_name}' using Google Gemini API...")
        
        api_key = st.secrets.get("gemini", {}).get("api_key", os.environ.get("GEMINI_API_KEY", ""))
        if not api_key:
            raise ValueError("API Key Gemini tidak ditemukan. Harap tambahkan ke .streamlit/secrets.toml atau environment variable GEMINI_API_KEY.")
            
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
        Tugas Anda adalah mengevaluasi kecocokan antara Resume (CV) kandidat dengan Deskripsi Pekerjaan (Job Description).
        
        Job Description:
        {job_description}
        
        Resume:
        {resume_text[:8000]}
        
        Berikan evaluasi Anda dalam format JSON yang tepat dengan struktur berikut:
        {{
            "score": [Berikan skor bulat antara 0 hingga 100 berdasarkan kecocokan],
            "analysis": "[Berikan 2 kalimat penjelasan singkat dalam bahasa Indonesia mengapa kandidat ini cocok atau tidak cocok]",
            "skills_matched": ["[Skill 1]", "[Skill 2]", "[Skill 3]"],
            "recommendation": "[Pilih salah satu: 'Highly Recommended', 'Recommended', 'Review Further', 'Not Recommended']"
        }}
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                safety_settings=[
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE,
                    ),
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE,
                    ),
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE,
                    ),
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE,
                    ),
                ],
            ),
        )
        
        result_text = response.text.strip()
        result = json.loads(result_text)
        
        # Ensure fallback for recommendation
        valid_recs = ["Highly Recommended", "Recommended", "Review Further", "Not Recommended"]
        if result.get("recommendation") not in valid_recs:
            score = result.get("score", 0)
            if score >= 80: result["recommendation"] = "Highly Recommended"
            elif score >= 65: result["recommendation"] = "Recommended"
            elif score >= 50: result["recommendation"] = "Review Further"
            else: result["recommendation"] = "Not Recommended"
            
        logger.info(f"AI_AGENT: Score={result.get('score')} | Recommendation={result.get('recommendation')} | Candidate={candidate_name}")
        return result

    except Exception as e:
        logger.error(f"AI_AGENT: Error for '{candidate_name}': {e}")
        return {"score": 0, "analysis": f"Evaluation failed: {str(e)}", "skills_matched": [], "recommendation": "Review Manually"}

def process_bulk_resumes(uploaded_files: list, job_description: str) -> list[dict]:
    """
    Process multiple PDF resumes in bulk.
    Returns list of result dicts with all evaluation data.
    """
    results = []
    logger.info(f"BULK_AGENT: Starting bulk processing of {len(uploaded_files)} resumes.")
    for i, pdf_file in enumerate(uploaded_files):
        filename = getattr(pdf_file, "name", f"resume_{i+1}.pdf")
        candidate_name = filename.replace(".pdf", "").replace("_", " ").replace("-", " ").title()
        logger.info(f"BULK_AGENT: Processing [{i+1}/{len(uploaded_files)}] '{filename}'")
        text = extract_text_from_pdf(pdf_file)
        ai_result = evaluate_resume_with_ai(text, job_description, candidate_name)
        results.append({
            "filename": filename,
            "candidate_name": candidate_name,
            "resume_text": text[:500] + "..." if len(text) > 500 else text,
            "score": ai_result.get("score", 0),
            "analysis": ai_result.get("analysis", ""),
            "skills_matched": ai_result.get("skills_matched", []),
            "recommendation": ai_result.get("recommendation", "Review Manually"),
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    logger.info(f"BULK_AGENT: Completed. Top score: {results[0]['score'] if results else 'N/A'}")
    return results
