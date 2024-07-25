### Variable Naming and Assignment


SUBMIT_SOLUTION = False


def assign_variables():
    # TODO: assign a string value to the variable `string_var`
    string_var = "randomstring"

    # TODO: assign an integer value to the variable `integer_var`
    integer_var = 12

    # TODO: assign a float value to the variable `float_var`
    float_var = 12.34

    # TODO: assign a boolean value to the variable `boolean_var`
    boolean_var = True

    return locals()


def fix_data_types():
    # TODO: change the code below to assign `string_var` a string value
    string_var = "680.55"

    # TODO: change the code below to assign `integer_var` an integer value
    integer_var = 12

    # TODO: change the code below to assign `float_var` a float value
    float_var = 12.34

    # TODO: change the code below to assign `boolean_var` a boolean value
    boolean_var = True

    return locals()


def cast_data_types():
    # TODO: convert the value into a string type using the str() function
    string_var = str(12)

    # TODO: convert the value into an integer type using the int() function
    integer_var = int(12.34)

    # TODO: convert the value into a float type using the float() function
    float_var = float(12)

    # TODO: convert the value into a boolean type using the bool() function
    boolean_var = bool(0)

    return locals()
