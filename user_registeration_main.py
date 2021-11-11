import pytest
import user_registeration

list_of_emails = []
correct_emails = [
    "abc-100@yahoo.com", "abc@yahoo.com", "abc.100@yahoo.com", "abc111@abc.com",
    "abc-100@abc.net", "abc.100@abc.com.au", "abc@1.com", "abc@gmail.com.com", "abc+100@gmail.com"
 ]
incorrect_emails = [
    "abc", "abc@.com.my", "abc123@gmail.a", "abc123@.com", "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com",
    "abc@%*.com", "abc..2002@gmail.com", "abc.@gmail.com", "abc@abc@gmail.com", "abc@gmail.com.1a",
    "abc@gmail.com.aa.au"
]

for email in correct_emails:
    list_of_emails.append((email, True))

for email in incorrect_emails:
    list_of_emails.append((email, False))


def test_first_name():
    assert not user_registeration.validate_first_name("harsh")
    assert user_registeration.validate_first_name("Harsh")


def test_last_name():
    assert not user_registeration.validate_last_name("ja")
    assert user_registeration.validate_first_name("Jain")


@pytest.mark.parametrize("email,expected", list_of_emails)
def test_email(email, expected):
    assert user_registeration.validate_email(email) == expected


def test_phone():
    assert not user_registeration.validate_phone("789 456 1232")
    assert user_registeration.validate_phone("+91 9874561230")


def test_password():
    assert not user_registeration.validate_password("okay1@34")
    assert not user_registeration.validate_password("Okay1234")
    assert not user_registeration.validate_password("")
    assert user_registeration.validate_password("pa2@Word")
