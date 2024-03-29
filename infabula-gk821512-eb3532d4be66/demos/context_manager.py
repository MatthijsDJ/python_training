class ContextManager:
    def __init__(self, expected_ex):
        print("Initializing")
        self.expected_ex = expected_ex

    def __enter__(self):
        print("Entering")

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print("Exception type:", ex_type)
        if self.expected_ex == ex_type:
            print("correcte exceptie")
        print("Exception value:",ex_value)
        print("Exiting")
        return False

if __name__ == "__main__":
    cm = ContextManager()
    print("in context")
    with ContextManager() as cm:
        print("context body code")
        try:
            value = int("vijf")
        except Exception as e:
            print(e))
        # raise ValueError()

