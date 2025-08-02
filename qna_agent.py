import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",  
)


chat_history = [
    {"role": "system", "content": "You are a helpful and responsible AI assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break


    chat_history.append({"role": "user", "content": user_input})

    try:

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=chat_history
        )


        ai_reply = response.choices[0].message.content
        print("AI:", ai_reply)
        chat_history.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        print("❌ Error:", e)

