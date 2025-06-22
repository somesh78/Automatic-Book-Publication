import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY", "your-groq-api-key"))

def spin_chapter(text: str) -> str:
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Rewrite this chapter in modern, engaging prose:\n\n" + text}],
    )
    return resp.choices[0].message.content
