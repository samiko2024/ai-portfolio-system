from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(data_text):
    prompt = f"""
    Analyze this portfolio data and generate a professional executive summary:
    - Performance overview
    - Risks
    - Recommendations

    {data_text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI service temporarily unavailable. Error: {str(e)}"
        return f"⚠️ AI service temporarily unavailable. Error: {str(e)}"