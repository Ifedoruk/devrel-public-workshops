from datetime import datetime
from airflow.decorators import dag, task


@dag(
    dag_display_name="4. Exercise: top_level_code",
    start_date=datetime(2023, 1, 1),
    max_active_runs=3,
    schedule=None,
    catchup=False,
    tags=["exercise", "exercise_4"],
)
def top_level_code():

    #### EXERCISE 4 ####
    @task
    def some_func():
        from include.helper_functions import expensive_api_call
        the_meaning_of_life_the_universe_and_everything = expensive_api_call()
        
        return the_meaning_of_life_the_universe_and_everything

    @task
    def reveal_the_meaning_of_life_the_universe_and_everything(the_answer):
        print(f"The meaning of life, the universe, and everything is... {the_answer}.")

    reveal_the_meaning_of_life_the_universe_and_everything(
        the_answer=some_func()
    )


top_level_code()
