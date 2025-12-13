import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

async def generate_reply(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "ごめん、ちょっと今頭が回らないみたい(AIエラー)。後でもう一度聞いてみて。"
