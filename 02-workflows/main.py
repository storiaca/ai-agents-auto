import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(usr_input: str) -> str:
    # call AI / LLM
    payload = {
        "model": "...S",
        "input": "..."
    }
    response = requests.post(
        "https://api.openai.com/v1/responses", 
        json=payload,
        headers= {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )
    pass
def main():
    # user input => AI (LLM) to generate X post => output post
    usr_input = input("What should post be about?")
    x_post = generate_x_post(usr_input)
    print("Generate X post")
    print((x_post))
if __name__ == "__main__":
    main()
