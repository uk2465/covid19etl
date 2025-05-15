# dags/covid_etl.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.extract import extract_covid_data
from scripts.transform import transform_covid_data
from scripts.load import load_to_postgres

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'covid_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for COVID-19 data',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['covid', 'etl'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract_covid_data',
        python_callable=extract_covid_data,
    )

    transform_task = PythonOperator(
        task_id='transform_covid_data',
        python_callable=transform_covid_data,
        op_args=["{{ ti.xcom_pull(task_ids='extract_covid_data') }}"],
    )

    load_task = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_to_postgres,
        op_args=["{{ ti.xcom_pull(task_ids='transform_covid_data') }}"],
    )

    extract_task >> transform_task >> load_task
