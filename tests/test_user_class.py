from pypractice import User
from pypractice import BadUserDictError

import inspect
import pytest


@pytest.fixture
def generic_user():
    return User(user_email="donotreply@nowhere.com", user_name="user42")


def test_user_has_user_id_property():
    assert hasattr(User, "user_id")


def test_user_id_is_not_none(generic_user):
    assert generic_user.user_id is not None


def test_user_has_user_email_property():
    assert hasattr(User, "user_email")


def test_user_email_must_be_valid():
    with pytest.raises(ValueError):
        _ = User(user_email="not-a-good-email-format@.com", user_name="user42")


def test_user_email_cannot_be_none():
    with pytest.raises(TypeError):
        _ = User(user_email=None, user_name="user42")


def test_user_email(generic_user):
    assert generic_user.user_email == "donotreply@nowhere.com"


def test_user_has_user_name_property():
    assert hasattr(User, "user_name")


def test_user_name_cannot_be_none():
    with pytest.raises(TypeError):
        _ = User(user_email="fake-email@nowhere.com", user_name=None)


def test_user_name(generic_user):
    assert generic_user.user_name == "user42"


def test_user_converts_to_dict(generic_user):
    user_dict = generic_user.to_dict()
    assert user_dict.get("user_name") == "user42"
    assert user_dict.get("user_email") == "donotreply@nowhere.com"
    assert user_dict.get("user_id") is not None


def test_user_from_dict_uuid_must_be_hexadecimal():
    with pytest.raises(ValueError):
        _ = User.from_dict(
            {
                # 'x' is an invalid hexadecimal character - otherwise good id
                "user_id": "db053c80-x973-46c2-9c1e-476eba467c63",
                "user_name": "user42",
                "user_email": "donotreply@nowhere.com",
            }
        )


def test_user_from_dict_email_must_be_valid(generic_user):
    with pytest.raises(ValueError):
        _ = User.from_dict(
            {
                "user_id": generic_user.user_id,
                "user_name": generic_user.user_name,
                "user_email": "bad-email-format",
            }
        )


def test_from_dict_passed_invalid_dictionary_keys():
    with pytest.raises(BadUserDictError):
        _ = User.from_dict(
            {"user_name": "user42", "user_email": "donotreply@nowhere.com"}
        )


def test_user_from_dict(generic_user):
    result = User.from_dict(generic_user.to_dict())
    assert result.user_id == generic_user.user_id
    assert result.user_name == generic_user.user_name
    assert result.user_email == generic_user.user_email
