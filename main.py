import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware 
from src.gemini import get_sentiment_from_gemini
from src.schemas import ReviewRequest, SentimentResponse

app = FastAPI(title="Secure Sentiment API")

# CORS Middleware Setup (Production Best Practice)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Public access / Cross-origin requests allowed
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST requests allowed
    allow_headers=["*"],
)

# Path checking list (tammam possible locations)  
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
POSSIBLE_PATHS = [
    os.path.join(CURRENT_DIR, "index.html"),  # src/ folder ke andar
    os.path.join(CURRENT_DIR, "..", "index.html"),  # secure_sentiment_api/ root mein
    os.path.join(os.getcwd(), "index.html"),  # terminal running directory mein
]


def find_index_file():
  for path in POSSIBLE_PATHS:
    abs_p = os.path.abspath(path)
    if os.path.exists(abs_p):
      return abs_p
  return None


@app.get("/", response_class=HTMLResponse)
def read_root():
  index_path = find_index_file()

  if not index_path:
    searched = "<br>".join([os.path.abspath(p) for p in POSSIBLE_PATHS])
    return HTMLResponse(
        content=f"<h2>⚠️ index.html Not Found!</h2><p>Python searched in these paths:<br><b>{searched}</b></p><p>Please ensure <code>index.html</code> is saved in one of these folders.</p>",
        status_code=404,
    )

  with open(index_path, "r", encoding="utf-8") as f:
    return f.read()


@app.post("/api/v1/analyze", response_model=SentimentResponse)
def analyze_sentiment(request: ReviewRequest):
  return get_sentiment_from_gemini(request.review_text)