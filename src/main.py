import os

from dotenv import load_dotenv
from google import genai


MODEL_NAME = "gemini-2.5-flash-lite"


def load_api_key() -> str:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to the local .env file."
        )

    return api_key


def main() -> None:
    print("=" * 50)
    print("Gemini Cloud AI Chatbot")
    print("Commands: /clear, /exit")
    print("=" * 50)

    # Keep the client alive for the entire application.
    client = genai.Client(api_key=load_api_key())

    chat = client.chats.create(
        model=MODEL_NAME,
    )

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
                    chat = client.chats.create(
                        model=MODEL_NAME,
                    )
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