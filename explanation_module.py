import os
import google.generativeai as genai

def explain_concept(topic: str):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))
        prompt = f"Explain the topic '{topic}' in simple terms for a student with examples."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error occurred while generating explanation: {e}"
