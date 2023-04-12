# import openai library
import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_PROJECT_TOKEN = os.getenv("OPENAI_PROJECT_TOKEN")
# Set up the OpenAI API client
openai.api_key = OPENAI_PROJECT_TOKEN


# this loop will let us ask questions continuously and behave like ChatGPT
def ask(prompt):
    # Set up the model and prompt
    model_engine = "text-davinci-003"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extracting useful part of response
    response = completion.choices[0].text

    # printing response
    return response
