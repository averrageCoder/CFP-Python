from contact import Contact
import json

address_book = []


class AddressBook:
    def __init__(self):
        self.address_book = []

    def add_contact(self, new_contact):
        """
        add contact to class variable
        :param contact: contact to be added
        :return: none
        """
        new_first_name = new_contact.first_name
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.first_name == new_first_name:
                print("Name already exists!")
                return
        self.address_book.append(new_contact)

    def edit_contact(self, person_to_edit, updated_contact):
        """
        ability to edit contact in addressbook using person firstname
        :param person_to_edit: first name of the person to be edited
        :param updated_contact: updated contact that needs to replaced
        :return: none
        """
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.first_name == person_to_edit:
                self.address_book[i] = updated_contact

    def __str__(self):
        """
        method to return object as string
        :return: object as string
        """
        string = ''
        if len(self.address_book) < 1:
            return "Nothing to show here!"
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            string += "Contact {}: {}\n".format(i + 1, contact)
        return string

    def delete_contact(self, person_to_delete):
        """
        ability to delete contact from addressbook
        :param person_to_delete: name of the person that needs to be deleted
        :return: none
        """
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.first_name == person_to_delete:
                self.address_book.remove(contact)
                return

    def search_person_by_state(self, state_to_search):
        """
        prints contact that matches the state
        :param state_to_search: state name to search by
        :return:
        """
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.state == state_to_search:
                print(contact)

    def search_person_by_city(self, city_to_search):
        """
        prints contact that matches the city
        :param city_to_search: city name to search by
        :return:
        """
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city == city_to_search:
                print(contact)

    def map_city_and_person(self):
        """
        to map city and person
        :return: dictionary with city person mapping
        """
        city_person_mapping = dict()
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city not in city_person_mapping.keys():
                city_person_mapping[contact.city] = [contact]
            else:
                city_person_mapping[contact.city].append(contact)
        return city_person_mapping

    def map_state_and_person(self):
        """
        to map state and person
        :return: dictionary with state person mapping
        """
        state_person_mapping = dict()
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city not in state_person_mapping.keys():
                state_person_mapping[contact.city] = [contact]
            else:
                state_person_mapping[contact.city].append(contact)
        return state_person_mapping

    def write_addressbook_to_json(self, json_filename):
        """
        ability to write addressbook to json
        :param json_filename: name of the file to be created
        :return: none
        """
        address_book_dict = {"addressbook": []}
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            address_book_dict["addressbook"].append(contact.__dict__())
        with open(json_filename, 'w') as fp:
            json.dump(address_book_dict, fp)

    def read_addressbook_from_json(self, json_filename):
        """
        read addressbook from json file
        :param json_filename: name of the json file to read from
        :return: none
        """
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
        """
        to get total contacts in the addressbook
        :return: total count of contacts
        """
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
