# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name  # name(name of company) is public
        self._proj = proj  # proj(current project) is protected
        self.__ccode = "code" # ccode is private

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self.__ccode)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name, " is ", self.__sal, self.show())


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)
# print(e.__sal)
print("Welcome to ", c.name)
print("Here ", e.name, " is working on ", e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()
c.show()