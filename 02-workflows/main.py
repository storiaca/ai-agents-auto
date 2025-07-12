from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

def generate_x_post(topic: str) -> str:
    with open("post-examples.json", "r") as f:
        examples = json.load(f)
    # Prepare examples for the prompt
    # examples_str = "\n\n".join(
    #     f"<topic>\n{example['topic']}\n</topic>\n\n<generated-post>\n{example['post']}\n</generated-post>"
    #     for example in examples
    # )
    examples_str = ""
    for i, example in enumerate(examples, 1):
        examples_str += f"""
        <example-{i}>
           <topic>
           {example['topic']}
           </topic>

           <generated-post>
           {example['post']}
           </generated-post>
        </example-{i}>
        """
    prompt = f"""
    You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).

    Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
    Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).

    Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.

    Here's the topic provided by the user for which you need to generate a post:
    <topic>
    {topic}
    </topic>

    Here are some examples of topic and generated posts:
    <examples>
        {examples_str}
    </examples>

    Please use the tone, language, structure, and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
    Don't use the content from the examples!
"""
    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )

    return response.output_text

def main():
    # user input => AI (LLM) to generate X post => output post
    usr_input = input("What should post be about?")
    x_post = generate_x_post(usr_input)
    print("Generate X post")
    print((x_post))
if __name__ == "__main__":
    main()
