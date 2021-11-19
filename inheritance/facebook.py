class FacebookUser:
    def __init__(self, first_name, last_name, friends_list):
        self.first_name = first_name
        self.last_name = last_name
        self.friends_list = friends_list

    def print_name(self):
        print(f'{self.first_name} {self.last_name}')

    def print_friends(self):
        print(f'{self.friends_list}')


if __name__ == '__main__':
    User1 = FacebookUser('Mike', 'Tyson', ['Buster Douglas', 'Evander Holyfied', 'Roy Jones Jr.'])
    User1.print_name()
    User1.print_friends()
