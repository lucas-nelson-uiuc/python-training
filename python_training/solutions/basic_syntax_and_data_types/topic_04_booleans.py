### {{ topic_name }}
# {{ topic_description }}


SUBMIT_SOLUTION = False


def boolean_comparison_operations():
    a = True
    b = False

    # TODO: complete the following statements comparing the numeric variables `a` and `b`
    boolean_equality = ...
    boolean_inequality = ...
    boolean_and = ...
    boolean_or = ...
    boolean_xor = ...

    return locals()


def boolean_truth_tables():
    # TODO: what is the result (True or False) of the following expression?
    boolean_expression = False or True or False or False
    boolean_result_1 = ...
    # TODO: what is the result (True or False) of the following expression?
    boolean_expression = False and True and True and True and True
    boolean_result_2 = ...
    # TODO: what is the result (True or False) of the following expression?
    boolean_expression = (False or True) and (False and False) or True
    boolean_result_3 = ...
    # TODO: what is the result (True or False) of the following expression?
    boolean_expression = ((not True and False) or True) and (
        not False and False or (True and not True)
    )
    boolean_result_4 = ...
    # TODO: what is the result (True or False) of the following expression?
    boolean_expression = False and not (
        True or not (False and not (True or not (False and not (True or False))))
    )
    boolean_result_5 = ...

    return locals()


def boolean_type_conversion():
    numeric_integer = 0
    numeric_float = 0.0001
    string_var = "random string"
    string_empty = ""

    # TODO: what is the result (True of False) of converting the follow variable to boolean?
    boolean_integer = bool(numeric_integer)
    boolean_result_1 = ...

    # TODO: what is the result (True of False) of converting the follow variable to boolean?
    boolean_float = bool(numeric_float)
    boolean_result_2 = ...

    # TODO: what is the result (True of False) of converting the follow variable to boolean?
    boolean_string_var = bool(string_var)
    boolean_result_3 = ...

    # TODO: what is the result (True of False) of converting the follow variable to boolean?
    boolean_string_empty = bool(string_empty)
    boolean_result_4 = ...

    return locals()


def string_formatting():
    currency = 9876543.21
    # TODO: assign the variable `full_name` as "First Last" using f-string formatting
    formatted_currency = ...

    return locals()


# [BONUS]
def boolean_truth_tables():
    # [PROMPT]
    # Regular expressions are useful for matching data against generic
    # patterns. Rather than knowing all possible email formats, we can specify
    # the generic pattern for any allowable email.
    #
    # The questions below make use of Python's regular expression module (re)
    # to make you familiar with simple - yet powerful - concepts of pattern
    # matching in Python.
    #
    # Please refer to the README file for this section to learn more about
    # regular expressions.

    # types of computers
    using_desktop = False
    using_laptop = True
    # types of computer inputs
    using_keyboard = True
    using_xbox_controller = False
    # types of programming languages
    using_python = True
    using_java = False

    # TODO: determine whether or not the user is using a computer
    using_computer = ...
    # TODO: determine whether or not the user is using one input
    using_one_input = ...
    # TODO: determine whether or not the user is only using an interpreted language
    using_interpreter = ...

    return locals()
