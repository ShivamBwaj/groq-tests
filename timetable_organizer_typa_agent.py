from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)
chat_history=[
    {"role": "system","content":"""You are a responsible AI study assistant.
Your job is to help the user create a personalized study schedule.
When asked, you will ask for subjects, number of topics, and total available hours per day.
Then break the topics down into a daily plan."""}
]

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit","quit"]:
       break
    chat_history.append({"role":"user","content": user_input})
    response=client.chat.completions.create(
        model="llama3-8b-8192",
        messages=chat_history,
        temperature=0.7, 
    )

    reply = response.choices[0].message.content
    print("AI: ", reply)
    chat_history.append({"role":"assistant","content": reply})

