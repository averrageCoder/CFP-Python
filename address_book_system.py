from contact import Contact

if __name__ == "__main__":
    address_books = []
    contact = Contact("James", "William", "12th Street", "London", "London",
                          "789456", "7894561230", "james@james.com")
    address_books.append(contact)
    print(contact)