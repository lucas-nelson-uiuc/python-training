import pytest
from python_training.topics.basic_syntax_and_data_types.exercises.topic_02_strings import (
    SUBMIT_SOLUTION,
    string_concatenation,
    string_escaping,
    string_formatting,
    string_repetition,
)


@pytest.mark.skipif(not SUBMIT_SOLUTION, reason="Solution not yet submitted")
class TestUserInput:
    def test_string_repetition(self):
        return_value = string_repetition().get("string_rep")
        assert isinstance(return_value, str)
        assert return_value == "randomrandomrandom"

    def test_string_concatenation(self):
        return_value = string_concatenation()
        return_keys = ("first_name", "last_name", "full_name")
        first_name, last_name, full_name = (
            return_value.get(var) for var in return_keys
        )
        assert all(isinstance(var, str) for var in (first_name, last_name, full_name))
        assert full_name == first_name + " " + last_name

    def test_string_formatting(self):
        return_value = string_formatting()
        return_keys = ("first_name", "last_name", "full_name")
        first_name, last_name, full_name = (
            return_value.get(var) for var in return_keys
        )
        assert all(isinstance(var, str) for var in (first_name, last_name, full_name))
        assert full_name == f"{first_name} {last_name}"

    def test_string_escaping(self):
        return_value = string_escaping()
        assert return_value.get("newline_char") == "\n"
        assert return_value.get("tab_char") == "\t"
