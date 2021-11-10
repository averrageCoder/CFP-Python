import re


def test_regex_pattern(pattern, source):
    if re.fullmatch(pattern, source):
        return True
    else:
        return False


def validate_name(name):
    pattern = "^[A-Z]{1}[a-z]{2,}$"
    return test_regex_pattern(pattern, name)


def validate_first_name(first_name):
    return validate_name(first_name)


def validate_last_name(last_name):
    return validate_name(last_name)




