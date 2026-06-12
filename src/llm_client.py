from google import genai
from google.genai import errors

from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_INSTRUCTION

def create_chat(client):
    """Create a fresh Gemini chat session."""

    return client.chats.create(
        model=MODEL_NAME,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
        },
    )

def create_client_and_chat():
    """Create the Gemini client and initial chat session."""

    client = genai.Client(api_key=GEMINI_API_KEY)
    chat = create_chat(client)

    return client, chat


def send_message(chat, prompt: str) -> str:
    """Send a message to Gemini and return the response text."""

    try:
        response = chat.send_message(prompt)

    except errors.APIError as error:
        if error.code == 429:
            raise RuntimeError(
                "Gemini free-tier quota has been reached. "
                "Try again after the daily quota resets or use Ollama locally."
            ) from error

        if error.code == 401:
            raise RuntimeError(
                "Gemini authentication failed. Check your API key."
            ) from error

        if error.code == 403:
            raise RuntimeError(
                "Your Gemini API key does not have permission for this request."
            ) from error

        raise RuntimeError(
            f"Gemini API request failed: {error.message}"
        ) from error

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text