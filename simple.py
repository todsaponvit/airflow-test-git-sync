from airflow.decorators import dag, task
from pendulum import datetime

@dag(start_date=datetime(2023, 1, 1), schedule=None, catchup=False)
def git_sync():

    @task
    def start():
        print("Pipeline started!")

git_sync()
