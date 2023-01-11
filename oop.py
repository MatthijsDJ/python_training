import datetime


flat_data = ('Eve', 'Janssen', 27)


data = {
    'first_name': 'Eva',
    'last_name': 'Janssen',
    'date_of_birth': 27
}


def update_person(data):
    data['age'] = -2


class Person:
    def __init__(self, 
                first_name: str, 
                last_name: str,
                date_of_birth: datetime.date,
                shoe_size: int=42) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.shoe_size = shoe_size

    def greet(self):
        print(f'Hallo {self.first_name} {self.last_name}')

    def get_age(self) -> int:
        
        now = datetime.date.today()
        delta = now - self.date_of_birth
        return delta.days // 365

    def is_adult(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

    def get_first_name(self) -> str:
        return self._first_name
    
    def set_first_name(self, first_name: str):
        if first_name:
            self._first_name = first_name
            return self
        else:
            raise ValueError

    first_name = property(get_first_name, set_first_name)

birth_date = datetime.date(year=2000, month=12, day=3)
person_1 = Person(first_name='Matthijs', last_name='de Jong', date_of_birth=birth_date, shoe_size=-1)
