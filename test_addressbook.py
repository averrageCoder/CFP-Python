import pytest
from contact import Contact
from address_book_system import AddressBook
from custom_address_book_error import AddressBookSystemError
import os


@pytest.fixture()
def address_book():
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


def test_add_contact_given_valid_inputs(address_book):
    """
    to test addition of contact on valid input
    :param address_book:
    :return:
    """
    assert address_book.get_total_contacts() == 2


def test_add_contact_given_invalid_first_name():
    """
    to test addition of contact on invalid input
    :return:
    """
    address_book = AddressBook()
    with pytest.raises(AddressBookSystemError) as e_info:
        contact1 = Contact("", "William", "12th Street", "London", "London",
                           "789456", "7894561230", "james@james.com")
        address_book.add_contact(contact1)
    assert address_book.get_total_contacts() == 0


def test_add_contact_given_invalid_last_name():
    """
    to test addition of contact when contact is invalid
    :return:
    """
    address_book = AddressBook()
    with pytest.raises(AddressBookSystemError) as e_info:
        contact1 = Contact("James", None, "12th Street", "London", "London",
                           "789456", "7894561230", "james@james.com")
        address_book.add_contact(contact1)


def test_edit_contact(address_book):
    """
    to test editing of contacts when name doesnt exist
    :param address_book:
    :return:
    """
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    person_to_edit = "JimmyNotHere"
    updated_contact = Contact("JimmyNotHere", "William", "21st Street", "Chennai", "TN",
                              "789456", "7894561230", "jimmy@james.com")
    with pytest.raises(AddressBookSystemError) as e_info:
        address_book.edit_contact(person_to_edit, updated_contact)


def test_delete_contact(address_book):
    """
    to test the deletion of contact
    :param address_book:
    :return:
    """
    person_to_delete = "Jimmy"
    address_book.delete_contact(person_to_delete)
    assert address_book.get_total_contacts() == 1


def test_city_person_mapping(address_book):
    """
    to test city person mapping
    :param address_book:
    :return:
    """
    city_person_mapping = address_book.map_city_and_person()
    assert city_person_mapping["Delhi"][0].first_name == "Jimmy"
    assert city_person_mapping["London"][0].first_name == "James"


# @pytest.mark.xfail
def test_state_person_mapping(address_book):
    """
    to test state person mapping
    :param address_book:
    :return:
    """
    state_person_mapping = address_book.map_state_and_person()
    assert state_person_mapping["Delhi"][0].first_name == "Jimmy"
    assert state_person_mapping["London"][0].first_name == "James"


def test_read_write_to_json(address_book):
    """
    to test reading and writing to json file
    :param address_book:
    :return:
    """
    json_filename = "addressbook.json"
    if os.path.isfile(json_filename):
        os.remove(json_filename)
    else:
        with pytest.raises(FileNotFoundError):
            os.remove(json_filename)
    address_book.write_addressbook_to_json(json_filename)
    assert os.path.isfile(json_filename)
    address_book.read_addressbook_from_json(json_filename)
    assert address_book.get_total_contacts() == 2


# @pytest.mark.xfail
def test_reading_data_from_json_when_no_file(address_book):
    """
    to test reading of addressbook when json file doesn't exist
    :param address_book:
    :return:
    """
    json_filename = "addressbook.json"
    with pytest.raises(FileNotFoundError):
        os.remove(json_filename)
        address_book.read_addressbook_from_json(json_filename)
