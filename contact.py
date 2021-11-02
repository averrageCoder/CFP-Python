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

    def __str__(self):
        """
        To return a string version of the object
        :return: string will all the object fields
        """
        return "first_name: {}, last_name: {}, address: {}, city: {}, state: {}, zip_code: {}, phone: {}, email: {} "\
                .format(self.first_name, self.last_name, self.address, self.city,
                        self.state, self.zip_code, self.phone, self.email)