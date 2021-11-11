from contact import Contact
from address_book_system import AddressBook
address_book = AddressBook()
JSON_FILENAME = "addressbook.json"

def get_choice():
    menu = "0. Exit\n" \
           "1. Add\n" \
           "2. Edit\n" \
           "3. Delete\n" \
           "4. Map city and person\n" \
           "5. Map state and person\n" \
           "6. Write to JSON\n" \
           "7. Read from JSON\n" \
           "99. Print addressbook\n" \
           "\nEnter your choice:"
    print(menu)
    choice = int(input())
    return choice


def add_contact_to_addressbook():
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    print("\nADDED SUCCESSFULLY")
    print("\nAFTER ADDING: \n", address_book)


def edit_contact_in_addressbook():
    print("Before Update!")
    print(address_book)

    person_to_edit = "Jimmy"
    updated_contact = Contact("Jimmy", "William", "21st Street", "Chennai", "TN",
                              "789456", "7894561230", "jimmy@james.com")

    address_book.edit_contact(person_to_edit, updated_contact)

    print("After Update!")
    print(address_book)


def delete_contact_in_addressbook():
    person_to_delete = "Jimmy"

    address_book.delete_contact(person_to_delete)

    print("After Delete!")
    print(address_book)


def map_city_to_person_in_addressbook():
    print("CITY PERSON MAPPING")
    city_person_mapping = address_book.map_city_and_person()
    for key, value in city_person_mapping.items():
        print("City: {}, Person Count: {}".format(key, len(value)))
        for contact in value:
            print(contact)


def map_state_to_person_in_addressbook():
    state_person_mapping = address_book.map_state_and_person()
    for key, value in state_person_mapping.items():
        print("State: {}, Person Count: {}".format(key, len(value)))
        for contact in value:
            print(contact)


def write_addressbook_to_json():
    print("Writing addressbook to json")
    address_book.write_addressbook_to_json(JSON_FILENAME)


def read_addressbook_from_json():
    print("Reading addressbook from json")
    address_book.read_addressbook_from_json(JSON_FILENAME)
    print(address_book)


if __name__ == "__main__":
    choice = get_choice()
    while True:
        if choice == 0:
            break
        elif choice == 99:
            print(address_book)
        elif choice == 1:
            add_contact_to_addressbook()
        elif choice == 2:
            edit_contact_in_addressbook()
        elif choice == 3:
            delete_contact_in_addressbook()
        elif choice == 4:
            map_city_to_person_in_addressbook()
        elif choice == 5:
            map_state_to_person_in_addressbook()
        elif choice == 6:
            write_addressbook_to_json()
        elif choice == 7:
            read_addressbook_from_json()
        choice = get_choice()
