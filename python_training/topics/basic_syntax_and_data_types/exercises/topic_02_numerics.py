### {{ topic_name }}
# {{ topic_description }}


SUBMIT_SOLUTION = False


def numeric_binary_operations():
    a = 193
    b = 17

    # TODO: complete the following statements evaluating the expression: `b` <operation> `a`
    numeric_sum = ...
    numeric_difference = ...
    numeric_product = ...
    numeric_exponentation = ...
    numeric_float_division = ...
    numeric_floor_division = ...
    numeric_modulus_division = ...

    return locals()


def numeric_comparison_operations():
    a = 193
    b = 17

    # TODO: complete the following statements comparing the numeric variables `a` and `b`
    numeric_greater_than = ...
    numeric_greater_than_equal_to = ...
    numeric_less_than = ...
    numeric_less_than_equal_to = ...
    numeric_equality = ...
    numeric_inequality = ...

    return locals()


def numeric_math_operations():
    import math

    radius = 25.4987

    # TODO: compute the following operations using math.<operation>(<radius>)
    radius_ceiling = ...
    radius_floor = ...
    radius_round_two_digits = ...
    radius_square_root = ...
    radius_is_infinity = ...

    # TODO: using the math module, complete the following formula for computing the area of a circle
    pi = ...
    radius_squared = ...  # try not to use the native power expression (`**`)
    circle_area = pi * radius_squared

    return locals()


def numeric_formatting():
    currency_int = 12345
    currency_float = 9876543.21
    currency_long_float = 9876.54321

    # TODO: format all currency variables such that they all:
    #   + start with a dollar sign ($)
    #   + separate places with commas
    #   + contain two - and only two - decimals
    formatted_int = ...
    formatted_float = ...
    formatted_long_float = ...

    return locals()


# [BONUS]
def statistics_builtin_module():
    import statistics

    # [PROMPT]
    # Python offers a collection of useful math-related packages, the statistics
    # package being one of them. These functions are useful for summarizing a
    # collection of numeric elements in a concise notation.
    #
    # Although there are third-party packages that offer more advanced
    # statistical methods (e.g. logistic regression, time series analysis,
    # bayesian statistics), we do not need these packages for computing simple
    # results.
    #
    # Complete the following exercises using the `statistics` package in Python.
    # Almost all results will be of the form `statistics.<operation>(grades)`

    grades = [78, 90, 56, 100, 80, 82, 94, 62, 77, 83, 83, 96]

    # TODO: what is the mode of all grades?
    grades_mean = ...
    # TODO: what is the mean of all grades?
    grades_mode = ...
    # TODO: what is the standard deviation of all grades?
    grades_stdev = ...
    # TODO: what is the variance of all grades?
    grades_variance = ...
    # TODO: which values occur multiple times?
    grades_multimode = ...
    # TODO: which of the multimode values occurs the most?
    grades_max_multimode = ...

    return locals()
