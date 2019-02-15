
import time
from airflow.operators import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

default_args = {
    'owner': 'Dewin Goh',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 18, 1),
    'retries': 1,
    'concurrency': 1,
    'max_active_runs': 1
}

def print_stuff():
	print("HELLO WORLD!!")
	time.sleep(5)
	print("HELLO AGAIN")

dag = DAG(
    dag_id='example_python_operator', default_args=default_args,
    schedule_interval=None)

task = PythonOperator(
    task_id='print_stuff',
    provide_context=True,
    python_callable=print_stuff,
    dag=dag)

