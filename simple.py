from airflow.decorators import dag, task
from pendulum import datetime

@dag(start_date=datetime(2023, 1, 1), schedule=None, catchup=False)
def my_first_dag():

    @task
    def start():
        print("Pipeline started!")

    start()
