import unittest
from unittest.mock import Mock
import etl.data_generator

class TestDataGenerator(unittest.TestCase):
    def test_names(self):
        with unittest.mock.patch('etl.data_generator.random_names') as mock_random_names:
            mocked_return = (('Tom', 'Tester'),)  # sequentie! want generator
            mock_random_names.return_value = mocked_return
            # call the function that uses random_names
            people = etl.data_generator.names(count=1)
            self.assertListEqual([mocked_return[0]], people)

