from groq import Groq
from app.config import get_settings
import json

settings = get_settings()
client = Groq(api_key=settings.groq_api_key)



def review_code(file_data: dict) -> dict:
  system_message = "You are a senior software engineer performing a code review. You provide clear, constructive feedback on code changes."
  user_message = (
    f"File: {file_data['filename']}\n"
    f"Added: {file_data['+']}\n"
    f"Removed: {file_data['-']}\n"
    f"Context: {file_data['context']}\n"
    """Respond in this exact JSON format:
    {
        "issues": [
            {
                "line": "the problematic line",
                "severity": "low/medium/high",
                "comment": "explanation",
                "suggestion": "improved code"
            }
        ],
        "summary": "overall feedback"
    }"""
  )
  response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
  )
  result = response.choices[0].message.content
  return json.loads(result)
