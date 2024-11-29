from airflow.decorators import dag
from airflow.datasets import Dataset
from airflow.operators.empty import EmptyOperator
from pendulum import datetime


@dag(
    start_date=datetime(2024, 8, 1),
    schedule=[Dataset("test_dataset")],
    catchup=False,
    tags=['igor_dags']
)
def my_consumer_dag():

    EmptyOperator(task_id="empty_task")


my_consumer_dag()