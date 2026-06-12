from config import APP_ENV, MODEL_NAME
from llm_client import create_chat, create_client_and_chat, send_message
from utils import is_clear_command, is_exit_command, print_header


def main() -> None:
    """Run the interactive Gemini chatbot."""

    print_header(
        title="Gemini Cloud AI Chatbot",
        environment=APP_ENV,
        model=MODEL_NAME,
    )

    client, chat = create_client_and_chat()

    try:
        while True:
            try:
                prompt = input("\nYou: ").strip()

                if not prompt:
                    continue

                if is_exit_command(prompt):
                    print("\nApp closed.")
                    break

                if is_clear_command(prompt):
                    chat = create_chat(client)
                    print("\nConversation history cleared.")
                    continue

                print("\nGemini: Thinking...\n")

                answer = send_message(chat, prompt)
                print(answer)

            except KeyboardInterrupt:
                print("\n\nApp closed.")
                break

            except Exception as error:
                print(f"\nError: {error}")

    finally:
        client.close()


if __name__ == "__main__":
    main()