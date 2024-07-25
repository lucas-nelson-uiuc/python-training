import pytest
import operator
from inspect import ismodule

from python_training.topics.basic_syntax_and_data_types.exercises.topic_02_numerics import (
    SUBMIT_SOLUTION,
    numeric_binary_operations,
    numeric_comparison_operations,
    numeric_math_operations,
    numeric_formatting,
    statistics_builtin_module
)


@pytest.mark.skipif(not SUBMIT_SOLUTION, reason="Solution not yet submitted")
class TestUserInput:
    def test_numeric_binary_operations(self):
        test_scope = numeric_binary_operations()
        a, b = test_scope.get("a"), test_scope.get("b")
        assert all(isinstance(var, (int, float)) for var in test_scope.values() if not ismodule(var))
        assert test_scope.get("numeric_sum") == operator.add(a, b)
        assert test_scope.get("numeric_difference") == operator.sub(a, b)
        assert test_scope.get("numeric_product") == operator.mul(a, b)
        assert test_scope.get("numeric_expoentiation") == operator.pow(a, b)
        assert test_scope.get("numeric_float_division") == operator.truediv(a, b)
        assert test_scope.get("numeric_floor_division") == operator.floordiv(a, b)
        assert test_scope.get("numeric_modulus_division") == operator.mod(a, b)

    def test_numeric_comparison_operations(self):
        test_scope = numeric_comparison_operations()
        a, b = test_scope.get("a"), test_scope.get("b")
        assert all(isinstance(var, bool) for var in test_scope.values()  if not ismodule(var))
        assert test_scope.get("numeric_greater_than") == operator.gt(a, b)
        assert test_scope.get("numeric_greater_than_equal_to") == operator.ge(a, b)
        assert test_scope.get("numeric_less_than") == operator.lt(a, b)
        assert test_scope.get("numeric_less_than_equal_to") == operator.le(a, b)
        assert test_scope.get("numeric_equality") == operator.eq(a, b)
        assert test_scope.get("numeric_inequality") == operator.ne(a, b)
        

    def test_numeric_math_operations(self):
        import math
        test_scope = numeric_math_operations()
        param_radius = test_scope.get("radius")
        assert all(isinstance(var, (int, float, bool)) for var in test_scope.values() if not ismodule(var))
        assert test_scope.get("radius_ceiling") == math.ceiling(param_radius)
        assert test_scope.get("radius_floor") == math.floor(param_radius)
        assert test_scope.get("radius_square_root") == math.sqrt(param_radius)
        assert test_scope.get("pi_is_finite") == math.isfinite(math.pi)
        assert test_scope.get("circle_area") == math.pi * math.pow(param_radius, 2)

    def test_numeric_formatting(self):
        test_scope = numeric_formatting()
        assert all(isinstance(var, (int, float, str)) for var in test_scope.values() if not ismodule(var))
        assert test_scope.get("formatted_int") == f"${test_scope.get('currency_int'):,.2f}"
        assert test_scope.get("formatted_float") == f"${test_scope.get('currency_float'):,.2f}"
        assert test_scope.get("formatted_long_float") == f"${test_scope.get('currency_long_float'):,.2f}"

    def test_statistics_builtin_module(self):
        import statistics
        test_scope = statistics_builtin_module()
        param_grades = test_scope.get("grades")
        assert all(isinstance(var, (int, float)) for var in test_scope.values() if not ismodule(var))
        assert test_scope.get("grades_mean") == statistics.mean(param_grades)
        assert test_scope.get("grades_mode") == statistics.mode(param_grades)
        assert test_scope.get("grades_stdev") == statistics.stdev(param_grades)
        assert test_scope.get("grades_variance") == statistics.variance(param_grades)
        assert test_scope.get("grades_multimode") == statistics.multimode(param_grades)
        assert test_scope.get("grades_max_multimode") == max(statistics.multimode(param_grades))
