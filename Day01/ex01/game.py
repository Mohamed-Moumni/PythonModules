class GotCharacter:
    """This class contains the first name and is_alive check attributes"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Lannister(GotCharacter):
    """This class Inherit from the base class GotCharacter"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.name_family = "Lannister"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
