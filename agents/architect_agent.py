"""
Technical Architect Agent — Anthropic Claude Edition
- Parses bulk PDF resumes using pypdf
- Evaluates against Job Description using Anthropic Claude API (Claude 3.5 Sonnet)
- 100% Clean from legacy Google Gemini imports
"""
import json
import io
import streamlit as st
from pypdf import PdfReader
import requests
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
    """Call Anthropic Claude API directly via HTTP Request."""
    if not resume_text:
        logger.warning(f"AI_AGENT: Empty resume text for '{candidate_name}'.")
        return {
            "score": 0, 
            "analysis": "Could not extract text from resume.", 
            "skills_matched": [], 
            "recommendation": "Review Manually"
        }

    try:
        # Ambil API Key Claude dari secrets.toml
        api_key = st.secrets["anthropic"]["api_key"]
        logger.info(f"AI_AGENT: Evaluating via Claude API for '{candidate_name}'...")

        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        system_prompt = "You are a senior HR analyst. Evaluate candidate resumes against job descriptions. Always respond ONLY with a single valid JSON object, no markdown blocks, no '```json' wrap, and no conversational text."

        user_prompt = f"""Evaluate this resume against the job description below.

JOB DESCRIPTION:
{job_description[:2000]}

RESUME:
{resume_text[:3000]}

Respond with EXACTLY this JSON structure:
{{
  "score": <integer 0-100>,
  "analysis": "<exactly 2 sentences: first on technical fit, second on recommendation>",
  "skills_matched": ["<skill1>", "<skill2>", "<skill3>"],
  "recommendation": "<one of: Highly Recommended | Recommended | Review Further | Not Recommended>"
}}"""

        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 800,
            "system": system_prompt,
            "messages": [
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2
        }

        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response_data = response.json()

        if response.status_code != 200:
            error_msg = response_data.get("error", {}).get("message", "Unknown Anthropic Error")
            raise Exception(f"Anthropic API Error ({response.status_code}): {error_msg}")

        raw_content = response_data["content"][0]["text"].strip()
        
        if "```" in raw_content:
            raw_content = raw_content.split("```")[1]
            if raw_content.startswith("json"):
                raw_content = raw_content[4:]
        raw_content = raw_content.strip()

        result = json.loads(raw_content)
        score = max(0, min(100, int(result.get("score", 0))))
        result["score"] = score
        
        return result

    except Exception as e:
        logger.error(f"AI_AGENT: Claude Evaluation failed for '{candidate_name}': {e}")
        return {
            "score": 0, 
            "analysis": f"Evaluation failed: {str(e)}", 
            "skills_matched": [], 
            "recommendation": "Review Manually"
        }


def process_bulk_resumes(uploaded_files: list, job_description: str) -> list[dict]:
    """Process multiple PDF resumes in bulk using Claude."""
    results = []
    for i, pdf_file in enumerate(uploaded_files):
        filename = getattr(pdf_file, "name", f"resume_{i+1}.pdf")
        candidate_name = filename.replace(".pdf", "").replace("_", " ").replace("-", " ").title()
        text = extract_text_from_pdf(pdf_file)
        ai_result = evaluate_resume_with_ai(text, job_description, candidate_name)
        results.append({
            "filename": filename,
            "candidate_name": candidate_name,
            "score": ai_result.get("score", 0),
            "analysis": ai_result.get("analysis", ""),
            "skills_matched": ai_result.get("skills_matched", []),
            "recommendation": ai_result.get("recommendation", "Review Manually"),
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
