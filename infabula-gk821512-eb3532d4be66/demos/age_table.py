import datetime
from person import Person
from pilot import Pilot


birth_date = datetime.date(year=2000, month=12, day=3)
person_1 = Person(first_name='Peter',
                  last_name='Bar',
                  birth_date=birth_date)

birth_date = datetime.date(year=2002, month=1, day=23)
person_2 = Pilot(first_name='Hans',
                 last_name='Janssen',
                 birth_date=birth_date,
                 skills="loopingspecialist")

people = [person_1, person_2]

def print_age(people):
    for person in people:
        print(f"{person.first_name}, {person.age()}")

def let_greet(people):
    for person in people:
        person.greet()


print_age(people)
let_greet(people)

