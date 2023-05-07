import typing

class GotCharacter:
    def __init__(self, first_name: str, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name: str = None, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    def __init__(self, first_name: str=None, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False
