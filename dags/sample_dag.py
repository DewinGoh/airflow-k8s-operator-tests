from datetime import datetime, timedelta

from airflow import DAG
from kubernetes import config

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
import logging


default_args = {
    'owner': 'Dewin Goh',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 18, 1),
    'retries': 1,
    'concurrency': 1,
    'max_active_runs': 1
}


dag = DAG('cloudfront-sg-update.update_sg_dag', default_args=default_args, schedule_interval='* * * * *')
job_name = 'cloudfront-sg-update.update-sg'


the_task = KubernetesPodOperator(namespace="airflow-test",
                                image="python:3.6-alpine",
                                cmds=["python","-c"],
                                arguments=["print('Hello World!')"],
                                in_cluster=True,
                                name="dag-test",
                                task_id="dag-test-task-id",
                                get_logs=True,
                                annotations={"iam.amazonaws.com/role": "api_access_role"},
                                is_delete_operator_pod=True,
                                dag=dag
                                )