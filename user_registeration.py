import re

from custom_user_registeration_errors import UserRegisterationError


def test_regex_pattern(pattern, source):
    if source is None:
        raise UserRegisterationError("Invalid input")
    if source == "":
        raise UserRegisterationError("Empty string passed")
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


def validate_email(email):
    pattern = '^abc([.+_-][A-Z0-9]+)?[A-Z0-9]*[@][A-Za-z0-9]+[\\.][A-Za-z]{2,}(.[A-Za-z]{2,6})?$'
    return test_regex_pattern(pattern, email)


def validate_phone(phone):
    pattern = "^([\\+]?\\d{2})?[\\s]?\\d{10}$"
    return test_regex_pattern(pattern, phone)


def validate_password(password):
    pattern = "^(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[\\S]{8,}$"
    return test_regex_pattern(pattern, password)

