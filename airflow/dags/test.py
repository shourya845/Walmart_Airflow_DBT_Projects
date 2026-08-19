import os

from databricks.sdk import WorkspaceClient

databricks_token = os.environ.get("DATABRICKS_TOKEN")
if not databricks_token:
    raise RuntimeError("DATABRICKS_TOKEN environment variable is required")

ws = WorkspaceClient(
    host=os.environ.get("DATABRICKS_HOST", "https://dbc-72b54f5e-b6fd.cloud.databricks.com"),
    token=databricks_token
)

# Trigger the job run
job_trigger = ws.jobs.run_now(job_id=879886565368122)

# Print the trigger response object (contains run_id)
print(job_trigger)
