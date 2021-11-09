import pytest
from contact import Contact
from address_book_system import AddressBook
import os

def test_add_contact():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    assert address_book.get_total_contacts() == 2


def test_edit_contact():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    person_to_edit = "Jimmy"
    updated_contact = Contact("Jimmy", "William", "21st Street", "Chennai", "TN",
                              "789456", "7894561230", "jimmy@james.com")
    address_book.edit_contact(person_to_edit, updated_contact)
    assert address_book.get_total_contacts() == 2


def test_delete_contact():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    person_to_delete = "Jimmy"
    address_book.delete_contact(person_to_delete)
    assert address_book.get_total_contacts() == 1


def test_city_person_mapping():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    city_person_mapping = address_book.map_city_and_person()
    assert city_person_mapping["Delhi"][0] == contact2
    assert city_person_mapping["London"][0] == contact1


def test_state_person_mapping():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    state_person_mapping = address_book.map_state_and_person()
    assert state_person_mapping["Delhi"][0] == contact2
    assert state_person_mapping["London"][0] == contact1


def test_read_write_to_json():
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    json_filename = "addressbook.json"
    address_book.write_addressbook_to_json(json_filename)
    assert os.path.isfile(json_filename)
    address_book.read_addressbook_from_json(json_filename)
    assert address_book.get_total_contacts() == 2
