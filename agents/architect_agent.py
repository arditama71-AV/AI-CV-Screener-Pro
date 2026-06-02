"""
Technical Architect Agent — Claude API Edition (Clean Build)
- PDF parsing via pypdf
- AI evaluation via anthropic SDK (claude-sonnet-4-20250514)
- Zero legacy imports (no google.genai, no openai, no raw requests)
"""
import json
import io
import streamlit as st
from pypdf import PdfReader
import anthropic
from utils.logger import get_logger

logger = get_logger("architect_agent")


def extract_text_from_pdf(pdf_file) -> str:
    """Extract full text from a PDF using pypdf."""
    try:
        if hasattr(pdf_file, "read"):
            reader = PdfReader(io.BytesIO(pdf_file.read()))
        else:
            reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        logger.info(f"PDF_AGENT: Extracted {len(text)} chars.")
        return text.strip()
    except Exception as e:
        logger.error(f"PDF_AGENT: Extraction failed — {e}")
        return ""


def evaluate_resume_with_ai(
    resume_text: str,
    job_description: str,
    candidate_name: str = "Candidate"
) -> dict:
    """
    Evaluate a resume against a JD using the Anthropic Claude SDK.
    Returns: {score, analysis, skills_matched, recommendation}
    """
    fallback = {
        "score": 0,
        "analysis": "Could not extract text from resume.",
        "skills_matched": [],
        "recommendation": "Review Manually"
    }

    if not resume_text.strip():
        logger.warning(f"AI_AGENT: Empty resume for '{candidate_name}'. Skipping.")
        return fallback

    try:
        api_key = st.secrets["anthropic"]["api_key"]
        client  = anthropic.Anthropic(api_key=api_key)

        logger.info(f"AI_AGENT: Evaluating '{candidate_name}'...")

        system_prompt = (
            "You are a senior HR analyst at a world-class enterprise organization. "
            "Evaluate candidate resumes against job descriptions with precision and fairness. "
            "Always respond ONLY with a single valid JSON object. "
            "No markdown fences, no backticks, no explanation — raw JSON only."
        )

        user_prompt = f"""Evaluate this resume against the job description below.

JOB DESCRIPTION:
{job_description[:2500]}

RESUME:
{resume_text[:3500]}

Return EXACTLY this JSON structure:
{{
  "score": <integer 0-100>,
  "analysis": "<exactly 2 sentences: first on technical/skills fit, second on overall recommendation>",
  "skills_matched": ["<skill1>", "<skill2>", "<skill3>"],
  "recommendation": "<one of: Highly Recommended | Recommended | Review Further | Not Recommended>"
}}"""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=600,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}]
        )

        raw = message.content[0].text.strip()

        # Defensive: strip markdown fences if model adds them
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        result = json.loads(raw)
        result["score"] = max(0, min(100, int(result.get("score", 0))))

        logger.info(
            f"AI_AGENT: Score={result['score']} | "
            f"Rec={result.get('recommendation')} | "
            f"Candidate={candidate_name}"
        )
        return result

    except json.JSONDecodeError as e:
        logger.error(f"AI_AGENT: JSON parse error for '{candidate_name}': {e} | raw={raw[:200]}")
        return {**fallback, "analysis": "AI response could not be parsed. Try again."}
    except anthropic.AuthenticationError:
        logger.error("AI_AGENT: Invalid API key. Check [anthropic] api_key in secrets.toml.")
        return {**fallback, "analysis": "Invalid API key. Check your Anthropic credentials."}
    except anthropic.RateLimitError:
        logger.error("AI_AGENT: Rate limit hit.")
        return {**fallback, "analysis": "Rate limit reached. Please wait and try again."}
    except Exception as e:
        logger.error(f"AI_AGENT: Unexpected error for '{candidate_name}': {e}")
        return {**fallback, "analysis": f"Evaluation failed: {str(e)}"}


def process_bulk_resumes(uploaded_files: list, job_description: str) -> list[dict]:
    """
    Process multiple PDF resumes in bulk.
    Returns list of result dicts sorted by score descending.
    """
    results = []
    total = len(uploaded_files)
    logger.info(f"BULK_AGENT: Starting — {total} resumes.")

    for i, pdf_file in enumerate(uploaded_files):
        filename = getattr(pdf_file, "name", f"resume_{i+1}.pdf")
        candidate_name = (
            filename.replace(".pdf", "")
                    .replace("_", " ")
                    .replace("-", " ")
                    .title()
        )
        logger.info(f"BULK_AGENT: [{i+1}/{total}] '{filename}'")
        text      = extract_text_from_pdf(pdf_file)
        ai_result = evaluate_resume_with_ai(text, job_description, candidate_name)
        results.append({
            "filename":       filename,
            "candidate_name": candidate_name,
            "score":          ai_result.get("score", 0),
            "analysis":       ai_result.get("analysis", ""),
            "skills_matched": ai_result.get("skills_matched", []),
            "recommendation": ai_result.get("recommendation", "Review Manually"),
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    top = results[0]["score"] if results else "N/A"
    logger.info(f"BULK_AGENT: Done. Top score={top}")
    return results
