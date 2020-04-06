from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'image': 'etl-application',
    'owner': 'airflow',
    'network_mode': 'etl-network',
    # 'docker_url': '/var/run/docker.sock',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=60),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
dag = DAG(
    'IEEE',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=20),
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = DockerOperator(
    task_id='identities',
    command='python ./etl_src/entry_point.py --job_and_func=ETLs.IEEE.identities_etl.identities_etl --start_date=2017-04-25 --end_date=2017-05-15',
    dag=dag,
)

t2 = DockerOperator(
    task_id='transactions',
    command='python ./etl_src/entry_point.py --job_and_func=ETLs.IEEE.transactions_etl.transactions_etl --start_date=2017-04-25 --end_date=2017-05-15',
    dag=dag
)
dag.doc_md = __doc__

t1.doc_md = """\
#### Identities etl
see etl_src/ETLs/IEEE/identities_etl.py
"""

t2.doc_md = """\
#### Transactions etl
see etl_src/ETLs/IEEE/transactions_etl.py
"""

t1 >> t2