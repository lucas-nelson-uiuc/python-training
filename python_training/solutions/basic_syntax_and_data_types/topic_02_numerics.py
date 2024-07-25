### {{ topic_name }}
# {{ topic_description }}


SUBMIT_SOLUTION = False


def numeric_binary_operations():
    a = 193
    b = 17

    # TODO: complete the following statements evaluating the expression: `b` <operation> `a`
    numeric_sum = a + b
    numeric_difference = a - b
    numeric_product = a * b
    numeric_exponentation = a ** b
    numeric_float_division = a / b
    numeric_floor_division = a // b
    numeric_modulus_division = a % b

    return locals()


def numeric_comparison_operations():
    a = 193
    b = 17

    # TODO: complete the following statements comparing the numeric variables `a` and `b`
    numeric_greater_than = a > b
    numeric_greater_than_equal_to = a >= b
    numeric_less_than = a < b
    numeric_less_than_equal_to = a <= b
    numeric_equality = a == b
    numeric_inequality = a != b

    return locals()


def numeric_math_operations():
    import math

    radius = 25.4987

    # TODO: compute the following operations using math.<operation>(<radius>)
    radius_ceiling = math.ceil(radius)
    radius_floor = math.floor(radius)
    radius_square_root = math.sqrt(radius)
    pi_is_finite = math.isfinite(math.pi)

    # TODO: using the math module, complete the following formula for computing the area of a circle
    pi = math.pi
    radius_squared = math.pow(radius, 2)
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
    formatted_int = f"${currency_int:,.2f}"
    formatted_float = f"${currency_float:,.2f}"
    formatted_long_float = f"${currency_long_float:,.2f}"

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
    grades_mean = statistics.mean(grades)
    # TODO: what is the mean of all grades?
    grades_mode = statistics.mode(grades)
    # TODO: what is the standard deviation of all grades?
    grades_stdev = statistics.stdev(grades)
    # TODO: what is the variance of all grades?
    grades_variance = statistics.variance(grades)
    # TODO: which values occur multiple times?
    grades_multimode = statistics.multimode(grades)
    # TODO: which of the multimode values occurs the most?
    grades_max_multimode = max(statistics.multimode(grades))

    return locals()
