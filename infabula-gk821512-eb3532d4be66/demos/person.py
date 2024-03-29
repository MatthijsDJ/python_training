import datetime

class Person:
    def __init__(self, *args, **kwargs) -> None:
        self.first_name = kwargs.get('first_name', 'UNDEFINED')
        self.last_name = kwargs.get('last_name', 'UNDEFINED')
        self.birth_date = kwargs.get('birth', None)
        self.shoe_size = kwargs.get('shoe_size', 42)

    def greet(self):
        print(f'Hallo ik ben {self.first_name} {self.last_name}.')

    def get_first_name(self) -> str:
        # check of iemand rechten heeft om de naam op te vragen
        return self._first_name

    def set_first_name(self, first_name: str) -> None:
        if first_name:
            self._first_name = first_name
            return self
        else:
            raise ValueError

    def age(self) -> int:
        now = datetime.date.today()
        delta = now - self.birth_date
        return delta.days // 365

    def is_adult(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

    first_name = property(get_first_name, set_first_name)
