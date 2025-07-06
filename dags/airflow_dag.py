import sys
sys.path.append('/opt/airflow')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# ✅ Correct imports based on your file names
from scripts.extract import extract_reddit
from scripts.transform import transform_reddit
from scripts.upload import upload_to_s3_main


default_args = {
    'owner': 'aniket',
    'start_date': datetime(2025, 6, 28),
    'retries': 1
}

with DAG(
    dag_id='reddit_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_reddit_posts',
        python_callable=extract_reddit
    )

    transform_task = PythonOperator(
        task_id='transform_posts',
        python_callable=transform_reddit
    )

    load_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3_main
    )

    extract_task >> transform_task >> load_task
