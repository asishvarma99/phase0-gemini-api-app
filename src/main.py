from config import APP_ENV, MODEL_NAME
from llm_client import create_chat, create_client_and_chat, send_message
from logger import get_logger
from utils import is_clear_command, is_exit_command, print_header


logger = get_logger(__name__)


def main() -> None:
    """Run the interactive Gemini chatbot."""

    print_header(
        title="Gemini Cloud AI Chatbot",
        environment=APP_ENV,
        model=MODEL_NAME,
    )

    client, chat = create_client_and_chat()

    logger.info(
        "Application started. Environment=%s Model=%s",
        APP_ENV,
        MODEL_NAME,
    )

    try:
        while True:
            try:
                prompt = input("\nYou: ").strip()

                if not prompt:
                    continue

                if is_exit_command(prompt):
                    logger.info("Application closed by user.")
                    print("\nApp closed.")
                    break

                if is_clear_command(prompt):
                    chat = create_chat(client)
                    logger.info("Conversation history cleared.")
                    print("\nConversation history cleared.")
                    continue

                print("\nGemini: Thinking...\n")

                answer = send_message(chat, prompt)
                print(answer)

            except KeyboardInterrupt:
                logger.info("Application interrupted by user.")
                print("\n\nApp closed.")
                break

            except Exception as error:
                logger.exception("Application error occurred.")
                print(f"\nError: {error}")

    finally:
        client.close()
        logger.info("Gemini client closed.")


if __name__ == "__main__":
    main()