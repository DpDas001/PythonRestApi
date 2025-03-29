#connect to openai and invoke completions

from openai import OpenAI

client = OpenAI()
def invoke(prompt):
    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )
    return response.output_text.strip()
