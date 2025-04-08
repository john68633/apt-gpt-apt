import openai
import os

def ask_gpt(prompt: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 부동산 전문 분석가입니다."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
