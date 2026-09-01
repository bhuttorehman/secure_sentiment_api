import json
import os

from dotenv import load_dotenv
from fastapi import HTTPException
from google import genai


# .env file se environment variables load karein
load_dotenv()


# Gemini API key read karein
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable missing hai!"
    )


# Gemini client create karein
client = genai.Client(api_key=api_key)


def get_sentiment_from_gemini(review_text: str):

    try:

        # Prompt
        prompt = f"""
Analyze the sentiment of the following customer review:

"{review_text}"

Return JSON ONLY with these exact keys:

{{
    "sentiment": "Positive",
    "confidence": 0.95,
    "summary": "Short 1-sentence summary of the review"
}}

The sentiment must be exactly one of:
Positive
Negative
Neutral

Confidence must be a number between 0 and 1.
"""


        # Gemini API call
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )


        # Gemini response ko Python dictionary mein convert karein
        result = json.loads(response.text)


        # Result return karein
        return result


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Gemini API Processing Error: {str(e)}"
        )