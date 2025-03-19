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

## Airflow DAG with Python Operator  

## Data Sharing via Airflow XComs  

## Airflow Task Flow API  

## Airflow Catch-Up and Backfill  

## Airflow Scheduler with Cron Expression  

## Airflow Connection to Postgres
package requirement:

**python==5.10.10**

**apache-airflow-providers-postgres==5.1.0**
1. Add on in docker-compose.yaml and write code in the file `dag_with_postgres_operator.py`

Check out the code in the file `dag_with_postgres_operator.py`.

sequence of task in code: `task1 >> task3 >> task2`

Why need task3? **If we try to delete one of the successful insert task, it tries to insert data which is already exists in the table. In the end, it will fail since violate the primary key constraint. Delete before insert can solve this issue.**

```bash
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    ports:
      - 5432:5432
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
```
2. Run the code in powershell in Visual Studio
```bash
docker-compose up -d --no-deps --build postgres
```
3. Download Dbeaver and create a new file. **Username** and **Password** can be found in `docker-compose.yaml`
<picture width="100">
  <img
    src="https://github.com/WaiYongF/Airflow/blob/main/Images/Airflow%20Connection%20to%20Postgres/Image_1.png"
    alt="Selection of Postgres Connection in Dbeaver"
  />
</picture>


<picture width="100">
  <img
    src="https://github.com/WaiYongF/Airflow/blob/main/Images/Airflow%20Connection%20to%20Postgres/dbeaver.PNG"
    alt="Selection of Postgres Connection in Dbeaver"
  />
</picture>

4. In Airflow, Admin -> Connection

<picture width="100">
  <img
    src="https://github.com/WaiYongF/Airflow/blob/cf6f4af97d0d7db29b75151a28910245bfb4e911/Images/Airflow%20Connection%20to%20Postgres/image.png"
    alt="Selection of Postgres Connection in Dbeaver"
  />
</picture>

5. Write PostgreSQL in dbeaver script

<picture width="100">
  <img
    src="https://github.com/WaiYongF/Airflow/blob/main/Images/Airflow%20Connection%20to%20Postgres/dbeaver_sql.PNG"
    alt="Selection of Postgres Connection in Dbeaver"
  />
</picture>

## Airflow Postgres Operator  

## Airflow Docker Install Python Package  

## Airflow AWS S3 Sensor Operator  

## Airflow Hooks S3 PostgreSQL  



