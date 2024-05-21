# Description of exercise

import pytest


SUBMIT_SOLUTION = False


def user_input():
    ### TODO: ...
    pass


# @pytest.mark.parametrize()
@pytest.mark.skipif(not SUBMIT_SOLUTION, reason="Solution not yet submitted")
class TestUserInput:
    def test_first_case(self):
        assert user_input() is None

    def test_second_case(self):
        assert user_input() is None

    def test_third_case(self):
        assert user_input() is None
