import datetime

flat_data = ('Eve', 'Janssen', 27)

data = {'first_name': 'Eva',
        'last_name': 'Janssen',
        'age': 27}


def update_person(data):
    data['age'] = -2


class Person:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birth_date: datetime.date,
                 shoe_size: int = 42) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.shoe_size = shoe_size

    def greet(self):
        print(f'Hallo ik ben {self.first_name} {self.last_name}.')

    def get_first_name(self) -> str:
        # check of iemand rechten heeft om de naam op te vragen
        print("getter first_name")
        return self._first_name

    def set_first_name(self, first_name: str) -> None:
        print("Setter first_name")
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

birth_date = datetime.date(year=2000, month=12, day=3)
person_1 = Person(first_name='Peter', last_name='Bar', birth_date=birth_date)

