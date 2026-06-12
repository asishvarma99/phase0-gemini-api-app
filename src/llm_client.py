from typing import Any

from google import genai
from google.genai import errors

from config import GEMINI_API_KEY, MODEL_NAME
from logger import get_logger
from prompts import SYSTEM_INSTRUCTION


logger = get_logger(__name__)


def create_chat(client: genai.Client) -> Any:
    """Create a fresh Gemini chat session."""

    return client.chats.create(
        model=MODEL_NAME,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
        },
    )


def create_client_and_chat() -> tuple[genai.Client, Any]:
    """Create the Gemini client and initial chat session."""

    client = genai.Client(api_key=GEMINI_API_KEY)
    chat = create_chat(client)

    return client, chat


def send_message(chat: Any, prompt: str) -> str:
    """Send a message to Gemini and return its response text."""

    logger.info("Sending request to Gemini model: %s", MODEL_NAME)

    try:
        response = chat.send_message(prompt)

    except errors.APIError as error:
        logger.error(
            "Gemini API error. Status=%s Message=%s",
            error.code,
            error.message,
        )

        if error.code == 429:
            raise RuntimeError(
                "Gemini rate limit or free-tier quota has been reached. "
                "Wait and try again later, or use Ollama locally."
            ) from error

        if error.code == 401:
            raise RuntimeError(
                "Gemini authentication failed. Check your API key."
            ) from error

        if error.code == 403:
            raise RuntimeError(
                "Gemini permission denied. Check the API key and project access."
            ) from error

        raise RuntimeError(
            f"Gemini API request failed: {error.message}"
        ) from error

    if not response.text:
        logger.warning("Gemini returned an empty response.")
        raise RuntimeError("Gemini returned an empty response.")

    logger.info("Gemini response received successfully.")

    return response.text