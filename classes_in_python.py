import re

from custom_exceptions import ContactCustomException


class UserDetails:
    def __init__(self, *params):
        print("constructor called")
        self.first_name = params[0][0]
        self.last_name = params[0][1]

    @property
    def first_name(self):
        print("getter called")
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        print("setter called")
        if value is None:
            raise ContactCustomException("Name cannot be none!")
        if re.fullmatch("^[A-Z]{1}[a-z]{2,}$", value):
            raise ContactCustomException("Name should have atleast 2 characters and should start with uppercase")

        self._first_name = value

    @property
    def last_name(self):
        print("getter for last name called")
        return self._last

    @last_name.setter
    def last_name(self, value):
        print("setter for last name called")
        self._last = value

    def __str__(self):
        return self.first_name + "__" + self.last_name


user1 = UserDetails(("Draco", "Malfoy"))
try:
    user1.first_name = "Nope"
    print(user1)
except ContactCustomException as exception:
    print(exception.__str__())
