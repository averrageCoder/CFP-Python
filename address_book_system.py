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


def search_person_by_state(state_to_search):
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.state == state_to_search:
            print(contact)

def search_person_by_city(city_to_search):
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.city == city_to_search:
            print(contact)


def map_city_and_person():
    city_person_mapping = dict()
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.city not in city_person_mapping.keys():
            city_person_mapping[contact.city] = [contact]
        else:
            city_person_mapping[contact.city].append(contact)
    return city_person_mapping


def map_state_and_person():
    state_person_mapping = dict()
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.city not in state_person_mapping.keys():
            state_person_mapping[contact.city] = [contact]
        else:
            state_person_mapping[contact.city].append(contact)
    return state_person_mapping


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

    address_book.append(contact2)
    state_to_search = "London"
    print("Searching state: {}".format(state_to_search))
    search_person_by_state(state_to_search)

    city_to_search = "Delhi"
    print("Searching city: {}".format(city_to_search))
    search_person_by_city(city_to_search)

    print("CITY PERSON MAPPING")
    city_person_mapping = map_city_and_person()
    for key, value in city_person_mapping.items():
        print("City: {}, Person Count: {}".format(key, len(value)))
        for contact in value:
            print(contact)

    print("STATE PERSON MAPPING")
    state_person_mapping = map_state_and_person()
    for key, value in city_person_mapping.items():
        print("State: {}, Person Count: {}".format(key, len(value)))
        for contact in value:
            print(contact)
