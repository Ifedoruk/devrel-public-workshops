from airflow.decorators import dag, task
from airflow.datasets import Dataset


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    tags=['igor_dags']
)
def my_producer_dag():

    @task(outlets=[Dataset("test_dataset")])
    def my_producer_task():
        pass

    my_producer_task()


my_producer_dag()
