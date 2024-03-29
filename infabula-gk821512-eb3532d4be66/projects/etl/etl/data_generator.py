from collections import namedtuple
import time
import requests

def timeit(old_function):
    def new_function(*args, **kwargs):
        start = time.perf_counter()
        result = old_function(*args, **kwargs)
        end = time.perf_counter()
        delta = end - start
        print(f"{old_function.__name__} took {delta} seconds.")
        return result
    return new_function



def random_names():
    url = "https://randomuser.me/api"
    while True:
        response = requests.get(url)
        data = response.json()
        if data:
            first_name = data["results"][0]['name']['first']
            last_name = data["results"][0]['name']['last']
            yield (first_name, last_name)

@timeit
def names(count=10):
    people = []
    if not count:
        return people
    for index, person in enumerate(random_names(), 1):
        if index > count:
            break
        print(person)
        people.append(person)
        # first_name, last_name = person
        #print(f"{first_name} {last_name}")

    return people

Person = namedtuple('Person', 'first_name last_name')

def names_as_dict():
    for item in random_names():
        p = Person(item)
        print(p.first_name)

def write_random_names(filename, count):
    with open(filename, 'w') as outfile:
        for index, person in enumerate(random_names()):
            first_name, last_name = person
            outfile.write(f"{first_name},{last_name}\n")
            if index > count:
                break

#write_random_names("names.csv", 20)