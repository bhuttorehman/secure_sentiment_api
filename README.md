## 🌟 Key Features

- **Input Validation Guardrails:** Automatically detects empty strings or whitespace-only inputs (`.strip()`) and raises a structured `400 Bad Request` error before reaching the AI model.
- **Strict Data Schemas:** Utilises **Pydantic** `BaseModel` schemas to validate payload structure and prevent malformed data type submissions (`422 Unprocessable Entity`).
- **Google Gemini Integration:** Powered by the modern `google-genai` SDK using `gemini-2.5-flash` for fast, cost-effective inference.
- **Environment Security:** Built with strict `.env` key isolation and `.gitignore` guardrails to prevent secret credential leaks.
- **Global Error Handling:** Implements robust `try-except` blocks to handle API failures gracefully with structured `500 Internal Server Error` responses.

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.12+
- **AI Engine:** Google GenAI SDK (`gemini-2.5-flash`)
- **Validation:** Pydantic
- **ASGI Server:** Uvicorn
- **Environment Security:** `python-dotenv`

---

## 📁 Repository Structure

```text
secure_sentiment_api/
│
├── main.py              # Core FastAPI application & route controllers
├── schemas.py           # Pydantic data validation schemas
├── requirements.txt     # Python dependency list
├── .env.example         # Template for environment configuration
├── .gitignore           # Security rules for blocking secret key leaks
└── README.md            # Project documentation & manual
⚡ Quick Start Guide
1. Clone the Repository
git clone https://github.com/bhuttorehman/secure_sentiment_api.git
cd secure_sentiment_api
2. Set Up Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure API Key
Create a .env file in the root directory (refer to .env.example):
GEMINI_API_KEY=your_actual_gemini_api_key_here
5. Launch the Local Server
uvicorn main:app --reload
Access interactive API documentation at: http://127.0.0.1:8000/docs
📡 API Endpoint Documentation
POST /ask
Analyzes review text and returns structured AI-grounded sentiment analysis.
Sample Request Payload (JSON):
{
  "prompt": "This product exceeded my expectations! The quality is amazing."
}
Successful Response (200 OK):
{
  "AI response": "Positive Sentiment: The review highlights high customer satisfaction with product quality and performance."
}
Handled Status Codes & Errors:
200 OK: Request processed successfully.
400 Bad Request: Raised when prompt is empty or contains only whitespace.
{
  "detail": "Prompt cannot be empty. Please provide review text."
}
422 Unprocessable Entity: Automatic Pydantic validation error for invalid data types.
500 Internal Server Error: Catches upstream API exceptions or missing environment configurations.
🔒 Security & Client Handover Rules
Zero Credential Leaks: The .env file is excluded via .gitignore to protect production API credentials.
Client Setup: A .env.example file is included so clients can safely plug in their own Gemini API keys upon deployment.
👤 Author
Abdul Rehman
AI Solutions Engineer in Training
GitHub: [bhuttorehman](https://github.com/bhuttorehman)
LinkedIn: [Abdul Rehman](https://www.linkedin.com/in/bhuttorehman)
