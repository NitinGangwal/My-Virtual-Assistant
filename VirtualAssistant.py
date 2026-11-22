#video-6
#Build an AI Powered Virtual Assistant
#Api key = Goodle gemini se free me banwayi h 
# Key ko environment variable me rakho (code me nahi)
import os
from openai import OpenAI

key = "(paste your api key here)"

client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

messages = []

def completion(message):
    messages.append({"role": "user", "content": message})
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="gemini-3.8-flash",
        )
    except Exception as e:
        print("ERROR:", e)
        print("Response body:", getattr(e, "body", None))
        messages.pop()  # failed user message hata do
        return
    
    reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Jarvis: {reply}")

if __name__ == "__main__":
    print("Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input("User: ")
        completion(user_question)

#Run = py d:/VirtualAssistant.py






