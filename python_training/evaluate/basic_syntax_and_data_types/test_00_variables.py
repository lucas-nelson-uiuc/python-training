import pytest
from python_training.topics.basic_syntax_and_data_types.exercises.topic_00_variables import (
    SUBMIT_SOLUTION,
    assign_variables,
    fix_data_types,
    cast_data_types,
)


@pytest.mark.skipif(not SUBMIT_SOLUTION, reason="Solution not yet submitted")
class TestUserInput:
    def test_assign_variables(self):
        test_scope = assign_variables()
        assert isinstance(test_scope.get("string_var"), str)
        assert isinstance(test_scope.get("integer_var"), int)
        assert isinstance(test_scope.get("float_var"), float)
        assert isinstance(test_scope.get("boolean_var"), bool)

    def test_fix_data_types(self):
        test_scope = fix_data_types()
        assert isinstance(test_scope.get("string_var"), str)
        assert isinstance(test_scope.get("integer_var"), int)
        assert isinstance(test_scope.get("float_var"), float)
        assert isinstance(test_scope.get("boolean_var"), bool)

    def test_cast_data_types(self):
        test_scope = cast_data_types()
        assert isinstance(test_scope.get("string_var"), str)
        assert isinstance(test_scope.get("integer_var"), int)
        assert isinstance(test_scope.get("float_var"), float)
        assert isinstance(test_scope.get("boolean_var"), bool)
