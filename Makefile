
.PHONY: dev data-sample train-local run-api eval-demo test

dev:
	pip install -r requirements.txt

data-sample:
	python data/synthetic_generators/gen_mobility.py --out data/samples/mobility_10k.csv --rows 10000

train-local:
	python ml/train_dummy_model.py --data data/samples/mobility_10k.csv --out serving/app/model.pkl

run-api:
	uvicorn serving.app.server:app --host 0.0.0.0 --port 8000 --reload

eval-demo:
	python ml/evaluate/cli.py --data data/samples/mobility_10k.csv --outdir outputs

test:
	pytest -q


run-stack:
	bash scripts/run_full_stack.sh

mlflow-demo:
	MLFLOW_TRACKING_URI=http://localhost:5000 python serving/app/mlflow_client_demo.py
