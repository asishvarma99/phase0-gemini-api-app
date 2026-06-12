from config import APP_ENV, MODEL_NAME
from llm_client import create_chat, create_client_and_chat, send_message


def main() -> None:
    print("=" * 50)
    print("Gemini Cloud AI Chatbot")
    print(f"Environment: {APP_ENV}")
    print(f"Model: {MODEL_NAME}")
    print("Commands: /clear, /exit")
    print("=" * 50)

    client, chat = create_client_and_chat()

    try:
        while True:
            try:
                prompt = input("\nYou: ").strip()

                if not prompt:
                    continue

                if prompt.lower() in {"/exit", "exit", "quit"}:
                    print("\nApp closed.")
                    break

                if prompt.lower() == "/clear":
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