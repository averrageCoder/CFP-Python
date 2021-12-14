import pytest
from contact import Contact
from address_book_system import AddressBook
from custom_address_book_error import AddressBookSystemError
import os


class TestClass:
    """ Class to test addressbook system"""

    @pytest.fixture()
    def address_book(self):
        """
        function to populate contacts to addressbook
        :return:
        """
        address_book = AddressBook()
        contact1 = Contact("James", "William", "12th Street", "London", "London",
                           "789456", "7894561230", "james@james.com")
        contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                           "789456", "7894561230", "jimmy@james.com")
        address_book.add_contact(contact1)
        address_book.add_contact(contact2)
        return address_book

    def test_delete_contact_given_invalid_name(self, address_book):
        """
        to test the deletion of contact given the name is invalid
        :param address_book:
        :return:
        """
        person_to_delete = "JimmyNotExists"
        with pytest.raises(AddressBookSystemError):
            address_book.delete_contact(person_to_delete)
            assert address_book.get_total_contacts() == 1
