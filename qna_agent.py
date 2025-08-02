import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 1: Load the .env file
load_dotenv()

# Step 2: Fetch your API key from environment
api_key = os.getenv("GROQ_API_KEY")

# Step 3: Check if the key exists
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

# Step 4: Create a Groq-compatible client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",  # THIS is what makes it talk to Groq, not OpenAI
)

# Step 5: Start an infinite loop (REPL - Read, Eval, Print Loop)
# Step 5: Start an infinite loop with memory
chat_history = [
    {"role": "system", "content": "You are a helpful and responsible AI assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    # Add user's message to chat history
    chat_history.append({"role": "user", "content": user_input})

    try:
        # Send entire chat history for context
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=chat_history
        )

        # Get AI's response
        ai_reply = response.choices[0].message.content
        print("AI:", ai_reply)

        # Add AI's response to history too
        chat_history.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        print("❌ Error:", e)
