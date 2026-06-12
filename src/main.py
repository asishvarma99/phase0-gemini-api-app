from google import genai

from config import APP_ENV, GEMINI_API_KEY, MODEL_NAME


def create_chat(client: genai.Client):
    """Create a new Gemini chat session."""

    return client.chats.create(
        model=MODEL_NAME,
    )


def main() -> None:
    """Run the interactive Gemini chatbot."""

    print("=" * 50)
    print("Gemini Cloud AI Chatbot")
    print(f"Environment: {APP_ENV}")
    print(f"Model: {MODEL_NAME}")
    print("Commands: /clear, /exit")
    print("=" * 50)

    client = genai.Client(api_key=GEMINI_API_KEY)
    chat = create_chat(client)

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

                response = chat.send_message(prompt)

                if not response.text:
                    print("Gemini returned an empty response.")
                    continue

                print(response.text)

            except KeyboardInterrupt:
                print("\n\nApp closed.")
                break

            except Exception as error:
                print(f"\nError: {error}")

    finally:
        client.close()


if __name__ == "__main__":
    main()