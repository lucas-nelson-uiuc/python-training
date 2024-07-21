### {{ topic_name }}
# {{ topic_description }}


SUBMIT_SOLUTION = False


def string_repetition():
    string_var = "random"
    # TODO: assign `string_rep` as the value of `string_var` repeated 3 times
    string_rep = ...

    return locals()


def string_concatenation():
    first_name = "First"
    last_name = "Last"
    # TODO: assign the variable `full_name` as "First Last" using string concatenation
    full_name = ...

    return locals()


def string_formatting():
    first_name = "First"
    last_name = "Last"
    # TODO: assign the variable `full_name` as "First Last" using f-string formatting
    full_name = ...

    return locals()


def string_escaping():
    # TODO: assign the variable `newline_character` as the newline escape sequence
    newline_char = ...
    # TODO: assign the variable `tab_character` as the tab escape sequence
    tab_char = ...

    return locals()


def string_indexing():
    string_var = "$680.55"
    # TODO: assign the variable `currency` as the currency sign from the `string_var` variable
    currency = ...
    # TODO: assign the variable `dollars` as the number of dollars from the `string_var` variable`
    dollars = ...
    # TODO: assign the variable `cents` as the number of cents from the `string_var` variable`
    cents = ...

    return locals()


def string_case_conversion():
    string_var = "RanDoMLY cAPITaLIzed StRiNG"
    # TODO: assign the variable `string_title` as the value of `string_var` in lower case
    string_lower = ...
    # TODO: assign the variable `string_title` as the value of `string_var` in upper case
    string_upper = ...
    # TODO: assign the variable `string_title` as the value of `string_var` in title case
    string_title = ...

    return locals()


def string_assertions():
    string_var = "random.email.99@python.org"
    # TODO: check if `string_var` starts with "random.email"
    is_random_email = ...
    # TODO: check if `string_var` ends with the domain "python.org"
    is_python_domain = ...
    # TODO: check if `string_var` contains digits in the username
    email_has_digit = ...

    return locals()


# [BONUS]
def string_pattern_matching():
    import re
    
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

    email = "random.email.99th@python.org"
    address = "123 99th St, Brooklyn, New York"
    
    # EXAMPLE: what is the username in the user's email address?
    username_pattern = "^([a-zA-Z0-9.]+)"
    email_username = (
        re.search(                          # using the search function ...
            re.compile(username_pattern),   # search for instances of the (compiled) pattern ...
            email                           # in the passed string ...
        )
        .group()                            # and return the matched instance (if there is one)
    )
    
    # TODO: what is the domain of the user's email address?
    domain_pattern = ...
    email_domain = ...
    # TODO: what city and state does the user live in?
    city_state_pattern = ...
    user_city = ...
    # TODO: return whether or not the user's street (99th) appears in their email
    street_pattern = ...
    user_street = ...
    check_street_in_email = ...

    return locals()
