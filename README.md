# 🤖 Secure Sentiment Analysis API & Web UI

A high-performance, modular FastAPI microservice integrated with Google's latest Gemini AI SDK for real-time customer review sentiment analysis.

## 🚀 Key Features
- **FastAPI Microservice**: High-speed asynchronous Python backend.
- **Gemini AI Integration**: Powered by Google GenAI SDK with structured JSON output enforcement.
- **Strict Data Validation**: Pydantic schemas for input payloads and output responses.
- **Interactive Web UI**: Modern HTML/CSS frontend with live API interaction.
- **Modular Architecture**: Industry-standard directory layout (`src/routers`, `src/schemas`, `src/gemini`).

## 🛠️ Tech Stack
- **Backend**: Python 3.12, FastAPI, Uvicorn
- **AI Engine**: Google GenAI SDK (`google-genai`)
- **Validation**: Pydantic v2, python-dotenv
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)

## 📦 Local Setup Instructions

1. **Activate Virtual Environment**:
   ```bash
   venv\Scripts\activate
Install Dependencies:
pip install fastapi uvicorn google-genai python-dotenv pydantic
Setup Environment Variables: Copy .env.example to .env and add your Gemini API Key:
GEMINI_API_KEY=your_actual_api_key_here
Run Application:
uvicorn src.main:app --reload
Access App:
Web UI: http://127.0.0.1:8000
Interactive Swagger API Docs: http://127.0.0.1:8000/docs

---