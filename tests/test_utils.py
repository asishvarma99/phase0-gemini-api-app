from src.utils import (
    is_clear_command,
    is_exit_command,
    normalize_command,
)

from src.utils import print_header


def test_print_header(capsys) -> None:
    print_header(
        title="Test App",
        environment="testing",
        model="test-model",
    )

    output = capsys.readouterr().out

    assert "Test App" in output
    assert "Environment: testing" in output
    assert "Model: test-model" in output
    assert "/clear" in output
    assert "/exit" in output

def test_normalize_command() -> None:
    assert normalize_command("  EXIT  ") == "exit"


def test_exit_commands() -> None:
    assert is_exit_command("/exit") is True
    assert is_exit_command("EXIT") is True
    assert is_exit_command("quit") is True
    assert is_exit_command("hello") is False


def test_clear_command() -> None:
    assert is_clear_command("/clear") is True
    assert is_clear_command("  /CLEAR  ") is True
    assert is_clear_command("clear") is False