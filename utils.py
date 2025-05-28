import os
from dotenv import load_dotenv
import openai
from qa_data import qa_pairs

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_hardcoded_answer(user_input):
    for pair in qa_pairs:
        if user_input.lower() in pair["question"].lower():
            return pair["answer"]
    return None

def get_fallback_answer(user_input):
    try:
        client = openai.OpenAI(api_key=openai.api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"
