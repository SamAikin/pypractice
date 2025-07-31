from .exceptions import BadUserDictError

import uuid
import re

_email_pattern = re.compile(
    r"(?:[a-z0-9\.\_\-])+\@(?:[a-z0-9\_\-])+\.[a-z]+", re.IGNORECASE
)

_uuid_pattern = re.compile(r"^(?:[a-f0-9\-]){36}$", re.IGNORECASE)


class User:
    """Class that holds state information about the user goals, skills, exercises, and evolutions are related to"""

    def __init__(self, user_email: str, user_name: str) -> None:
        if not check_email_format(user_email):
            raise ValueError("Bad Email Format Passed into User Initializer")
        if user_name is None:
            raise TypeError("None type object not allowed when initializing user")

        self._user_id: str = str(uuid.uuid4())
        self._user_email: str = user_email
        self._user_name: str = user_name

    @property
    def user_id(self) -> str:
        """Provides a read-only copy of the unique User ID generated"""
        return self._user_id

    @property
    def user_email(self) -> str:
        """Provides a read-only copy of the user's email"""
        return self._user_email

    @property
    def user_name(self) -> str:
        """Provides a read-only copy of the user's name"""
        return self._user_name

    def to_dict(self) -> dict:
        """Returns the User object as a dictionary; useful for serialization of object"""
        return {
            "user_id": self._user_id,
            "user_name": self._user_name,
            "user_email": self._user_email,
        }

    @classmethod
    def from_dict(cls, user_dict: dict) -> "User":
        """Class builder method to create a user object from a dictionary; useful when unserializing

        :param user_dict: the User instance variables to set - must include a valid uuid
        :type user_dict: dict
        :rtype: User
        """
        result = super().__new__(cls)
        try:
            if not check_uuid_format(user_dict["user_id"]):
                raise ValueError("Bad format on uuid passed to User constructor")
            if not check_email_format(user_dict["user_email"]):
                raise ValueError("Bad email format passed to User constructor")
            result._user_id = user_dict["user_id"]
            result._user_email = user_dict["user_email"]
            result._user_name = user_dict["user_name"]
        except KeyError:
            raise BadUserDictError()
        return result


def check_email_format(email: str) -> bool:
    """Accepts a string, and evaluates if it appears to be a valid email

    :param email: The string to check for email format compliance
    :type email: str
    :returns: whether string is a well formatted email
    :rtype: bool
    """
    if _email_pattern.search(email) is None:
        return False
    return True


def check_uuid_format(hexstr: str) -> bool:
    """Accepts a string and valids it only contains hexadecimal characters and dashes

    :param hexstr: input that is validated - must be only a-f 0-9 or a '-'
    :type hexstr: str
    :returns: Whether is a valid hexadecimal uuid string
    :rtype: bool
    """
    if _uuid_pattern.search(hexstr) is None:
        return False
    return True
