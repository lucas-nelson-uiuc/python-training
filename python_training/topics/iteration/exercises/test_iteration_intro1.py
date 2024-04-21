# Description of exercise

import pytest
import string


IGNORE_FILE = False


def user_input(characters: str) -> list[str]:
    return [char for char in characters]




@pytest.mark.parametrize(
    "characters",
    [string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters]
)
@pytest.mark.skipif(IGNORE_FILE, reason="User not ready")
def test_user_input(characters: str):
    assert user_input(characters) == list(characters)
