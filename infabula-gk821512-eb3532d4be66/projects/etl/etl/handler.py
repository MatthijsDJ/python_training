def read():
    print("Reading data.")

def transform():
    print("Transforming data.")

def process():
    print("Processing data")
    print("Filtering.")

def write():
    print("Writing results")

def run():
    data = read()
    transformed = transform(data)
    results = process(transformed)
    write(results)

if __name__ == "__main__":
    run()