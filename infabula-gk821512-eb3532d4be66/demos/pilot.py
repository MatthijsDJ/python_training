import datetime
from person import Person


class Pilot(Person):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.skills = kwargs.get('skills', '')

    def greet(self):  # method overriding
        print(f"Uw piloot {self.first_name} {self.last_name} meld zich met skills {self.skills}.")

