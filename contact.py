from custom_address_book_error import AddressBookSystemError
class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        """
        Constructor to initialize class object
        :param first_name: first name of person
        :param last_name: last name of person
        :param address: address of the person
        :param city: city of person
        :param state: state of person
        :param zip_code: zip code of person
        :param phone: phone number of the person
        :param email: email id of the person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    # a getter function
    @property
    def first_name(self):
        return self._first_name

    # a setter function
    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise AddressBookSystemError('Invalid first name')
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    # a setter function
    @last_name.setter
    def last_name(self, last_name):
        if not last_name or last_name.strip() == "":
            raise AddressBookSystemError('Invalid last name')
        self._last_name = last_name

    @property
    def address(self):
        return self._address

    # a setter function
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def city(self):
        return self._city

    # a setter function
    @city.setter
    def city(self, city):
        if not city or city.strip() == "":
            raise AddressBookSystemError('Invalid city')
        self._city = city

    # a getter function
    @property
    def state(self):
        return self._state

    # a setter function
    @state.setter
    def state(self, state):
        if not state or state.strip() == "":
            raise AddressBookSystemError('Invalid state')
        self._state = state

    @property
    def zip_code(self):
        return self._zip_code

    # a setter function
    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

    @property
    def phone(self):
        return self._phone

    # a setter function
    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    # a setter function
    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        """
        To return a string version of the object
        :return: string will all the object fields
        """
        return "first_name: {}, last_name: {}, address: {}, city: {}, state: {}, zip_code: {}, phone: {}, email: {} " \
            .format(self.first_name, self.last_name, self.address, self.city,
                    self.state, self.zip_code, self.phone, self.email)

    def __dict__(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone": self.phone,
            "email": self.email
        }
