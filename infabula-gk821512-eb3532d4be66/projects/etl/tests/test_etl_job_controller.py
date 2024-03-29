from etl import (ETLJobController,
                 ETLJob)


def test_add_job():
    """als er nieuwe jobrunner wordt aangemaakt
    en je voegt er vervolgens een job aan toe
    dan is daarna de het aantal jobs met 1 verhoogd
    """
    # setup
    job_controller = ETLJobController()
    job1 = ETLJob('job 1')
    # test code runnen
    job_controller.add_job(job1)
    # evaluatie
    assert len(job_controller.jobs) == 1