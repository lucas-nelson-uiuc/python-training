import pytest
from python_training.topics.type_hinting.exercises.topic_00_static import (
    SUBMIT_SOLUTION,
    # ... other tests here ...
)


# @pytest.mark.parametrize()
@pytest.mark.skipif(not SUBMIT_SOLUTION, reason="Solution not yet submitted")
class TestUserInput:
    def test_first_case(self):
        assert True

    def test_second_case(self):
        assert True

    def test_third_case(self):
        assert True