from contact import Contact
import json

address_book = []


class AddressBook():
    def __init__(self):
        self.address_book = []

    def add_contact(self, contact):
        self.address_book.append(contact)

    def edit_contact(self, person_to_edit, updated_contact):
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.first_name == person_to_edit:
                self.address_book[i] = updated_contact

    def __str__(self):
        string = ''
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            string += "Contact {}: {}\n".format(i + 1, contact)
        return string

    def delete_contact(self, person_to_delete):
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.first_name == person_to_delete:
                self.address_book.remove(contact)

    def search_person_by_state(self, state_to_search):
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.state == state_to_search:
                print(contact)

    def search_person_by_city(self, city_to_search):
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city == city_to_search:
                print(contact)

    def map_city_and_person(self):
        city_person_mapping = dict()
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city not in city_person_mapping.keys():
                city_person_mapping[contact.city] = [contact]
            else:
                city_person_mapping[contact.city].append(contact)
        return city_person_mapping

    def map_state_and_person(self):
        state_person_mapping = dict()
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city not in state_person_mapping.keys():
                state_person_mapping[contact.city] = [contact]
            else:
                state_person_mapping[contact.city].append(contact)
        return state_person_mapping

    def write_addressbook_to_json(self, json_filename):
        address_book_dict = {"addressbook": []}
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            address_book_dict["addressbook"].append(contact.__dict__())
        with open(json_filename, 'w') as fp:
            json.dump(address_book_dict, fp)

    def read_addressbook_from_json(self, json_filename):
        self.address_book = []
        with open(json_filename) as json_file:
            data = json.load(json_file)
        for contact in data["addressbook"]:
            first_name = contact["first_name"]
            last_name = contact["last_name"]
            address = contact["address"]
            city = contact["city"]
            state = contact["state"]
            zip_code = contact["zip_code"]
            phone = contact["phone"]
            email = contact["email"]
            self.address_book.append(Contact(first_name, last_name, address, city
                                             , state, zip_code, phone, email))

    def get_total_contacts(self):
        return len(self.address_book)


if __name__ == "__main__":
    address_book = AddressBook()
    contact1 = Contact("James", "William", "12th Street", "London", "London",
                       "789456", "7894561230", "james@james.com")
    contact2 = Contact("Jimmy", "William", "16th Street", "Delhi", "Delhi",
                       "789456", "7894561230", "jimmy@james.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    print("Before Update!")
    print(address_book)

    person_to_edit = "Jimmy"
    updated_contact = Contact("Jimmy", "William", "21st Street", "Chennai", "TN",
                              "789456", "7894561230", "jimmy@james.com")

    address_book.edit_contact(person_to_edit, updated_contact)

    print("After Update!")
    print(address_book)

    person_to_delete = "Jimmy"

    address_book.delete_contact(person_to_delete)

    print("After Delete!")
    print(address_book)

    address_book.add_contact(contact2)
    state_to_search = "London"
    print("Searching state: {}".format(state_to_search))
    address_book.search_person_by_state(state_to_search)

    city_to_search = "Delhi"
    print("Searching city: {}".format(city_to_search))
    address_book.search_person_by_city(city_to_search)

    print("CITY PERSON MAPPING")
    city_person_mapping = address_book.map_city_and_person()
    for key, value in city_person_mapping.items():
        print("City: {}, Person Count: {}".format(key, len(value)))
        for contact in value:
            print(contact)

    print("STATE PERSON MAPPING")
    state_person_mapping = address_book.map_state_and_person()
    for key, value in city_person_mapping.items():
        print("State: {}, Person Count: {}".format(key, len(value)))
        for contact in value:
            print(contact)

    print("Writing addressbook to json")
    json_filename = "addressbook.json"
    address_book.write_addressbook_to_json(json_filename)

    print("Reading addressbook from json")
    address_book.read_addressbook_from_json(json_filename)
    print(address_book)
