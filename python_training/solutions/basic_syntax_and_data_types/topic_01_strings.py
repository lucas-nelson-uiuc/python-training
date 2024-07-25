### {{ topic_name }}
# {{ topic_description }}


SUBMIT_SOLUTION = True


def string_repetition():
    string_var = "random"
    # TODO: assign `string_rep` as the value of `string_var` repeated 3 times
    string_rep = string_var * 3

    return locals()


def string_concatenation():
    first_name = "First"
    last_name = "Last"
    # TODO: assign the variable `full_name` as "First Last" using string concatenation
    full_name = first_name + " " + last_name

    return locals()


def string_formatting():
    first_name = "First"
    last_name = "Last"
    # TODO: assign the variable `full_name` as "First Last" using f-string formatting
    full_name = f"{first_name} {last_name}"

    return locals()


def string_escaping():
    # TODO: assign the variable `newline_character` as the newline escape sequence
    newline_char = "\n"
    # TODO: assign the variable `tab_character` as the tab escape sequence
    tab_char = "\t"

    return locals()


def string_indexing():
    string_var = "$680.55"
    # TODO: assign the variable `currency` as the currency sign from the `string_var` variable
    currency = string_var[0]
    # TODO: assign the variable `dollars` as the number of dollars from the `string_var` variable`
    dollars = string_var[1:4]
    # TODO: assign the variable `cents` as the number of cents from the `string_var` variable`
    cents = string_var[5:]

    return locals()


def string_case_conversion():
    string_var = "RanDoMLY cAPITaLIzed StRiNG"
    # TODO: assign the variable `string_title` as the value of `string_var` in lower case
    string_lower = string_var.lower()
    # TODO: assign the variable `string_title` as the value of `string_var` in upper case
    string_upper = string_var.upper()
    # TODO: assign the variable `string_title` as the value of `string_var` in title case
    string_title = string_var.title()

    return locals()


def string_assertions():
    string_var = "random.email.99@python.org"
    # TODO: check if `string_var` starts with "random.email"
    is_random_email = string_var.startswith("random.email")
    # TODO: check if `string_var` ends with the domain "python.org"
    is_python_domain = string_var.endswith("python.org")
    # TODO: check if `string_var` contains digits in the username
    email_has_digit = string_var[13:15].isdigit()

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
        re.search(  # using the search function ...
            re.compile(
                username_pattern
            ),  # search for instances of the (compiled) pattern ...
            email,  # in the passed string ...
        ).group()  # and return the matched instance (if there is one)
    )

    # TODO: what is the domain of the user's email address?
    domain_pattern = "([a-zA-Z.]+)$"
    email_domain = re.search(re.compile(domain_pattern), email).group()
    # TODO: what city and state does the user live in?
    city_state_pattern = "[a-zA-Z0-9\s]+,\s([a-zA-Z0-9\s,]+)$"
    user_city = re.search(re.compile(city_state_pattern), address).group()
    # TODO: return whether or not the user's street (99th) appears in their email
    street_pattern = "^[0-9]+\s([0-9]+)"
    user_street = re.search(re.compile(street_pattern), address).group()
    check_street_in_email = user_street in email

    return locals()
