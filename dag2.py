import datetime

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
##from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator


with DAG(
    dag_id="practice_2",
    schedule=None,
):
   
    def run_sql():
        opr_call_sproc1 = BigQueryOperator(
            task_id="example", 
            sql = """update_query.sql""",
        )

    run_sql()