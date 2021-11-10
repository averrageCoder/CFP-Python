import pytest
import user_registeration


def test_first_name():
    assert not user_registeration.validate_first_name("harsh")
    assert user_registeration.validate_first_name("Harsh")


def test_last_name():
    assert not user_registeration.validate_last_name("ja")
    assert user_registeration.validate_first_name("Jain")


def test_email():
    assert not user_registeration.validate_email("jaja.com")
    assert user_registeration.validate_email("abc.xyz@bl.co.in")


def test_phone():
    assert not user_registeration.validate_phone("789 456 1232")
    assert user_registeration.validate_phone("+91 9874561230")
