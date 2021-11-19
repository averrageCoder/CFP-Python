from facebook import FacebookUser


class SpotifyUser(FacebookUser):
    def __init__(self, first_name, last_name, friends_list, playlist):
        super().__init__(first_name, last_name, friends_list)
        self.playlist = playlist

    def get_playlist(self):
        print(f"{self.first_name} {self.last_name}'s playlist: {self.playlist}")


if __name__ == '__main__':
    user2 = SpotifyUser("Floyd", "Mayweather", ['Buster Douglas', 'Evander Holyfied', 'Roy Jones Jr.'],
                        ["Harry Styles", "Taylor Swift"])

    user2.print_name()
    user2.print_friends()

    user2.get_playlist()
