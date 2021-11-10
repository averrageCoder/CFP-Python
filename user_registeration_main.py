import pytest
import user_registeration


def test_first_name():
    assert not user_registeration.validate_first_name("harsh")
    assert user_registeration.validate_first_name("Harsh")
