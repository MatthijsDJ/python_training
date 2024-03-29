def true_false():
    print("van start")
    yield True
    print("Voorbij True")
    yield False
    print("Voorby False")

def diy_range(end):
    value = 0
    while value < end:
        yield value
        value += 1

def infinite():
    value = 0
    while True:
        yield value
        value += 1