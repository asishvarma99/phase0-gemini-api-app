import os

from dotenv import load_dotenv
from google import genai


MODEL_NAME = "gemini-2.5-flash-lite"


def load_api_key() -> str:
    """Load and validate the Gemini API key."""

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to the local .env file."
        )

    return api_key


def generate_response(prompt: str) -> str:
    """Send a prompt to Gemini and return the generated text."""

    client = genai.Client(api_key=load_api_key())

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text


def main() -> None:
    prompt = (
        "Explain the difference between local AI and cloud AI "
        "in exactly three concise bullet points."
    )

    print("Sending request to Gemini...\n")

    answer = generate_response(prompt)

    print("Gemini response:\n")
    print(answer)


if __name__ == "__main__":
    main()