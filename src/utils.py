def normalize_command(value: str) -> str:
    """Clean and normalize user commands."""

    return value.strip().lower()


def is_exit_command(value: str) -> bool:
    """Return True when the user wants to exit."""

    return normalize_command(value) in {
        "/exit",
        "exit",
        "quit",
    }


def is_clear_command(value: str) -> bool:
    """Return True when the user wants to clear chat history."""

    return normalize_command(value) == "/clear"


def print_header(
    title: str,
    environment: str,
    model: str,
) -> None:
    """Display the application header."""

    print("=" * 50)
    print(title)
    print(f"Environment: {environment}")
    print(f"Model: {model}")
    print("Commands: /clear, /exit")
    print("=" * 50)