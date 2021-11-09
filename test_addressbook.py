import pytest
from contact import Contact
from address_book_system import AddressBook
import os


@pytest.fixture()
def address_book():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    return address_book


def test_add_contact(address_book):
    assert address_book.get_total_contacts() == 2


def test_edit_contact(address_book):
    assert address_book.get_total_contacts() == 2


def test_delete_contact(address_book):
    person_to_delete = "Jimmy"
    address_book.delete_contact(person_to_delete)
    assert address_book.get_total_contacts() == 1


def test_city_person_mapping(address_book):
    city_person_mapping = address_book.map_city_and_person()
    assert city_person_mapping["Delhi"][0].first_name == "Jimmy"
    assert city_person_mapping["London"][0].first_name == "James"


def test_state_person_mapping(address_book):
    state_person_mapping = address_book.map_state_and_person()
    assert state_person_mapping["Delhi"][0].first_name == "Jimmy"
    assert state_person_mapping["London"][0].first_name == "James"


def test_read_write_to_json(address_book):
    json_filename = "addressbook.json"
    os.remove(json_filename)
    address_book.write_addressbook_to_json(json_filename)
    assert os.path.isfile(json_filename)
    address_book.read_addressbook_from_json(json_filename)
    assert address_book.get_total_contacts() == 2
