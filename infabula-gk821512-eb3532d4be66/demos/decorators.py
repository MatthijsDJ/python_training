import time

def uppercase(old_function):
    def new_function(first_name, last_name):
        first_name = "Anonymous"
        result = old_function(first_name, last_name)
        return result + " is nice"
    return new_function

@uppercase
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def authenticate(old_function):
    def inner(name):
        if name.lower()[0] == 'e':
            result = old_function(name)
            return result
        else:
            return f"{name} is helaas niet welkcom."
    return inner


@authenticate
def enter(name):
    return f"Welcome {name}!"

door_queue = ["Eve", "John", "Ellen", "Peter"]

for name in door_queue:
    print(enter(name))

def max_hundred(old_function):
    def new_function(first, second):
        result = old_function(first, second)
        if result > 100:
            result = 100
        return result
    return new_function


def max(max_value):
    def max_output(old_function):
        def new_function(first, second):
            result = old_function(first, second)
            if result > max_value:
                result = max_value
            return result
        return new_function
    return max_output


@max(100)
def add(first, second):
    return first + second

@max(50)
def multiply(first, second):
    return first * second


def timeit(old_function):
    def new_function(*args, **kwargs):
        start = time.perf_counter()
        result = old_function(*args, **kwargs)
        end = time.perf_counter()
        delta = end - start
        print(f"{old_function.__name__} took {delta} seconds.")
        return result
    return new_function
