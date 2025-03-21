from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'waiyongf',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2025, 3, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1=BashOperator(
        task_id='task1',
        bash_command='echo This is an simple bash command'
    )

#type in the terminal
# docker ps
# docker exec -it b0225242143f bash
# airflow dags backfill -s 2025-01-01 -e 2025-01-11 dag_with_catchup_backfill_v02