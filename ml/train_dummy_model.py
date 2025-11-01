import argparse, joblib, pandas as pd
from sklearn.linear_model import LogisticRegression
import os
import mlflow

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    df = pd.read_csv(args.data)
    X = df[['clicks_1h','clicks_24h','purchases_7d']].values
    y = df['y'].values
    clf = LogisticRegression(max_iter=200).fit(X, y)
    joblib.dump({'model': clf, 'features': ['clicks_1h','clicks_24h','purchases_7d']}, args.out)
    print(f'Saved model to {args.out}')
    # Optional: log to MLflow if tracking server is configured
    tracking = os.getenv("MLFLOW_TRACKING_URI")
    if tracking:
        mlflow.set_tracking_uri(tracking)
        with mlflow.start_run(run_name="dummy-train"):
            mlflow.log_param("model", "logreg")
            mlflow.log_param("features", "clicks_1h,clicks_24h,purchases_7d")
            mlflow.log_artifact(args.out)
            # quick metrics (train set for demo)
            acc = float((clf.predict(X) == y).mean())
            mlflow.log_metric("train_acc", acc)
            print(f"Logged run to MLflow at {tracking}, train_acc={acc:.3f}")

if __name__ == '__main__':
    main()
