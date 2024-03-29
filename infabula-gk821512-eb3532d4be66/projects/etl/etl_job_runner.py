from etl import (ETLJobController,
                 ETLJob)
from loan_etl_job import LoanETLJob


def main():
    job_controller = ETLJobController()
    job1 = ETLJob('job 1')
    job_controller.add_job(job1)
    job2 = LoanETLJob('job 2')
    job_controller.add_job(job2)
    job_controller.run_jobs()

main()