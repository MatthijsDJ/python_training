import sys
"""
Job container for ETL's
"""

class ETLPriorityError(Exception):
    pass

class ETLJob:  # base class
    """
    ETL class is a base class for ETL jobs
    """
    # class property
    id_counter = 0

    def __init__(self, name):
        ETLJob.id_counter += 1
        self.id = ETLJob.id_counter
        self.name = name
        self.last_run_timestamp = None
        self.priority = 0

    @property
    def priority(self):  # getter
        return self._priority

    @priority.setter
    def priority(self, value):
        if value < 0 or value > 9:
            raise ETLPriorityError("Value should be within range 0-9")
        self._priority = value

    def fail(self):
        self.log("Job failed.")

    def log(self, message):
        print(f"LOG['{self.name}': {message}")

    def run(self):
        print(f"run van job {self.name} is niet geimplementeerd.")

