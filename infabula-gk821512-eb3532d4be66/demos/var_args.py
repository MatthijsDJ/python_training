def fun_args(first, second, *args, **kwargs):
    print(f"first: {first}")
    print(f"second :{second}")
    print(f"*args :{args}")
    for key, value in kwargs.items():
        print(f"{key}->{value}")

def add(x, y, *args):
    extra_values = args
    total = x + y
    for value in extra_values:
        total += value
    return total

