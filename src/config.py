import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


def require_environment_variable(name: str) -> str:
    """Return a required environment variable or raise a clear error."""

    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"{name} is missing. Add it to the .env file in the project root."
        )

    return value


GEMINI_API_KEY = require_environment_variable("GEMINI_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash-lite",
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development",
)