# Apache Airflow

<picture width="500">
  <img
    src="https://github.com/apache/airflow/blob/19ebcac2395ef9a6b6ded3a2faa29dc960c1e635/docs/apache-airflow/img/logos/wordmark_1.png?raw=true"
    alt="Apache Airflow logo"
  />
</picture>

[Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

**Table of contents**

- [Airflow DAG with Bash Operator](#Airflow-DAG-with-Bash-Operator)  
- [Airflow DAG with Python Operator](#Airflow-DAG-with-Python-Operator)  
- [Data Sharing via Airflow XComs](#Data-Sharing-via-Airflow-XComs)  
- [Airflow Task Flow API](#Airflow-Task-Flow-API)  
- [Airflow Catch-Up and Backfill](#Airflow-Catch-Up-and-Backfill)  
- [Airflow Scheduler with Cron Expression](#Airflow-Scheduler-with-Cron-Expression)  
- [Airflow Connection to Postgres](#Airflow-Connection-to-Postgres)  
- [Airflow Postgres Operator](#Airflow-Postgres-Operator)  
- [Airflow Docker Install Python Package](#Airflow-Docker-Install-Python-Package)  
- [Airflow AWS S3 Sensor Operator](#Airflow-AWS-S3-Sensor-Operator)  
- [Airflow Hooks S3 PostgreSQL](#Airflow-Hooks-S3-PostgreSQL) 

## Airflow DAG with Bash Operator


