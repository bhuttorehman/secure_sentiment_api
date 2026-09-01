from pydantic import BaseModel, Field

# Client se aane wale Review data ki validation
class ReviewRequest(BaseModel):
    user_name: str
    user_age: int
    review_text: str = Field(
        ..., 
        min_length=1, 
        max_length=1000, 
        description="The text review left by the customer."
    )


# Client ko wapas bheje jane wale Response ka structure
class SentimentResponse(BaseModel):
    sentiment: str       # Positive, Negative, ya Neutral
    confidence: float    # Score e.g. 0.95 (95%)
    summary: str         # 1-sentence summary