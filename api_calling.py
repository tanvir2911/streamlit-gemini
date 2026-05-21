from google import genai
from dotenv import load_dotenv
import os

# loading the envirornment variable
load_dotenv()

api_key = os.getenv("GEMII_API_KEY")


# initializing a client
client = genai.Client(api_key=api_key)

def note_generator(images):
    prompt = """Summarize the picture in note format at max 100 words, 
    make sure to add necessary markdown to differentiate different sections"""
    response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[images, prompt]
        )
    return response.text