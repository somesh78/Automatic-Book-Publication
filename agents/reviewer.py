import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY", "your-groq-api-key"))

def review_chapter(text: str) -> str:
    prompt = "You are an expert editor. Improve clarity, flow & style:\n\n" + text
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content
