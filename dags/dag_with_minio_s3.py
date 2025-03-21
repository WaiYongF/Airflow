#to rerun the minio in the container after restart laptop, run:
# docker start minio1

# add connection in airflow
# type in extra
# {
#   "aws_access_key_id": "ROOTUSER",
#   "aws_secret_access_key": "CHANGEME123",
#   "host": "http://host.docker.internal:9000"
# }

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args={
    'owner': 'waiyongf',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_minio_s3_v02',
    start_date=datetime(2025, 3, 1),
    schedule_interval='@daily'
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minio_conn',
        mode='poke',
        poke_interval=5,
        timeout=30
    )