import pytest
import unittest
from etl import ETLJob, ETLPriorityError


def test_incremental_job_id():
    """
    setup: class id_counter is initieel 0
    als er een nieuw Job wordt aangemaakt
    dan moet de nieuwe job de job_id hebben met waarde 1
    en nadien moet de id_counter gelijk zijn aan 1
    """
    assert ETLJob.id_counter == 0
    job = ETLJob(name="test job")
    assert job.id == 1
    assert ETLJob.id_counter == 1


def test_priority_setting_valid_range():
    job = ETLJob(name="test job")
    job.priority = 9
    assert job.priority == 9


def test_priority_setting_invalid_range():
    """Raises an ValueError if priority is set to invalid value."""
    with pytest.raises(ETLPriorityError) as ve:
        job = ETLJob(name="test job")
        job.priority = -1


class TestPriority(unittest.TestCase):
    def setUp(self):
        self.job = ETLJob(name="test job")

    def test_priority_setting_valid_range(self):
        self.job.priority = 9
        self.assertEqual(self.job.priority, 9)

    def test_priority_setting_invalid_range(self):
        with self.assertRaises(ETLPriorityError) as error:
            self.job.priority = -2

    def tearDown(self):
        pass
