from contact import Contact

address_book = []


def edit_contact(person_to_edit, updated_contact):
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.first_name == person_to_edit:
            address_book[i] = updated_contact


def print_addressbook():
    for i in range(len(address_book)):
        contact = address_book[i]
        print("Contact {}: {}".format(i+1, contact))


def delete_contact(person_to_delete):
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.first_name == person_to_delete:
            address_book.remove(contact)


if __name__ == "__main__":
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.append(contact1)
    address_book.append(contact2)

    print("Before Update!")
    print_addressbook()

    person_to_edit = "Jimmy"
    updated_contact = Contact("Jimmy", "William", "21st Street", "Chennai", "TN",
                              "789456", "7894561230", "jimmy@james.com")

    edit_contact(person_to_edit, updated_contact)

    print("After Update!")
    print_addressbook()

    person_to_delete = "Jimmy"

    delete_contact(person_to_delete)

    print("After Delete!")
    print_addressbook()
