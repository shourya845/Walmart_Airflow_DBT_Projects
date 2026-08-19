import os
import time
from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import RunLifeCycleState, RunResultState


@dag
def orchestrate():

    @task
    def ingest_cdc():
        databricks_token = os.environ.get("DATABRICKS_TOKEN")
        if not databricks_token:
            raise RuntimeError("DATABRICKS_TOKEN environment variable is required")

        ws = WorkspaceClient(
            host=os.environ.get("DATABRICKS_HOST", "https://dbc-72b54f5e-b6fd.cloud.databricks.com"),
            token=databricks_token
        )

        job_trigger = ws.jobs.run_now(job_id=879886565368122)

        while True:
            job_run = ws.jobs.get_run(job_trigger.run_id)

            if job_run.state.life_cycle_state in [
                RunLifeCycleState.TERMINATED, 
                RunLifeCycleState.SKIPPED, 
                RunLifeCycleState.INTERNAL_ERROR
            ]:
                if job_run.state.result_state == RunResultState.SUCCESS:
                    print("Job completed successfully!")
                    break 
                else:
                    raise Exception(f"Job failed with state: {job_run.state.result_state}")
                    
            time.sleep(5)
        
        return "CDC Ingestion Completed"
    
    @task.bash
    def clean_target():
        return "rm -rf /opt/airflow/walmart_project/target && rm -rf /opt/airflow/walmart_project/logs"

    @task.bash
    def source_freshness():
        return "cd /opt/airflow/walmart_project && dbt source freshness"

    silver_technical = BashOperator(
        task_id='silver_technical',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select silver_t'
    )

    silver_technical_tests = BashOperator(
        task_id='silver_technical_tests',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt test --select silver_t'
    )

    silver_business = BashOperator(
        task_id='silver_business',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select silver_b'
    )

    silver_business_tests = BashOperator(
        task_id='silver_business_tests',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt test --select silver_b'
    )

    gold_dimensions = BashOperator(
        task_id='gold_dimensions',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt snapshot'
    )

    gold_facts = BashOperator(
        task_id='gold_facts',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select path:models/gold/fact+'
    )

    # Cleaned dependency flow without gold_ephemeral
    (
        ingest_cdc() 
        >> clean_target() 
        >> source_freshness() 
        >> silver_technical 
        >> silver_technical_tests 
        >> silver_business 
        >> silver_business_tests 
        >> gold_dimensions 
        >> gold_facts
    )

orchestrate_dag = orchestrate()
