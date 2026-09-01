from fastapi import APIRouter, HTTPException, status
from src.schemas import ReviewRequest, SentimentResponse
from src.gemini import analyze_sentiment

router = APIRouter(prefix="/api/v1", tags=["Sentiment Analysis"])

@router.post("/analyze", response_model=SentimentResponse, status_code=status.HTTP_200_OK)
def analyze_review_endpoint(payload: ReviewRequest):
    try:
        # Gemini AI ko call karna
        result = analyze_sentiment(payload.review_text)
        return result
        
    except ValueError as ve:
        # Agar .env mein API key missing ho (HTTP 500 Error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(ve)
        )
    except Exception as e:
        # Agar Gemini ka server down ho ya connection fail ho (HTTP 503 Error)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail=f"AI Service Error: {str(e)}"
        )
