import datetime
import json
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
##from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
file_path= '/home/airflow/gcs/data/config/config_${env_name}.json'
with open(file_path, 'r') as file:
    data=json.load(file)
    dataset1=data['dataset']

with DAG(
    dag_id="practice_6",
    schedule=None,
    user_defined_macros={"dataset": dataset1},
):
   
    def run_sql():
        opr_call_sproc1 = BigQueryOperator(
            task_id="example", 
            sql = """update_query.sql""",
            use_legacy_sql=False,
        )

    run_sql()