# Description of exercise

import pytest


IGNORE_FILE = True


def user_input():
    ### TODO: ...
    pass


@pytest.mark.skipif(IGNORE_FILE, reason="User not ready")
def test_user_input():
    ### TODO...
    assert user_input() is None