import os, mlflow, time, random
from mlflow import MlflowClient

def main():
    uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    mlflow.set_tracking_uri(uri)
    client = MlflowClient()
    exp = client.create_experiment("demo") if "demo" not in [e.name for e in client.list_experiments()] else None
    with mlflow.start_run(experiment_id=client.get_experiment_by_name("demo").experiment_id, run_name="quick-log") as run:
        for i in range(5):
            mlflow.log_metric("demo_metric", random.random(), step=i)
            time.sleep(0.1)
    print(f"Logged demo run to {uri}")

if __name__ == "__main__":
    main()
