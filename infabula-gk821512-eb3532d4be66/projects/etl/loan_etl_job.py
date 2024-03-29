from etl import ETLJob

class LoanETLJob(ETLJob):
    def __init__(self, name):
        super().__init__(name)
        self.data = {}

    def read(self):
        self.log("Reading load data")

    def transform(self):
        self.log("Transforming load data")

    def run(self):
        print(f"We runnen LOAN job {self.name}")
        self.read()
        self.transform()