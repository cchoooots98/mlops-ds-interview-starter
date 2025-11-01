# MLOps + Data Science Interview Starter (Public-safe)

This repository is a **public, privacy-safe, runnable skeleton** to demonstrate DS + MLOps skills
without exposing any real data, secrets, or company-specific details.

## What’s inside
- **Synthetic data generators** and small sample CSVs (reproducible)
- **SQL**: analytics + engineering patterns (funnels, retention, SCD2, keyset vs offset)
- **Feature engineering**: contracts (Pandera-style placeholder), rolling features templates
- **ML evaluation toolkit**: PR-AUC + threshold scan, calibration + Brier, PSI drift
- **Leakage scanner** and **feature importance stability (bootstrap)**
- **Local serving**: FastAPI API with a tiny trained model (no cloud needed)
- **Design docs & templates**: rollback runbook, AB measurement playbook, interview templates

> ⚠️ **No real data, secrets, or company names.** Use `.env.example` to configure your own secrets (do not commit `.env`).

## Quickstart
```bash
# 1) Python env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2) Generate synthetic data
make data-sample

# 3) Train a tiny local model (saved to serving/app/model.pkl)
make train-local

# 4) Run the local FastAPI server
make run-api

# 5) Try evaluation CLI (creates plots in outputs/)
make eval-demo

# 6) Run tests + linters
make test
```

## Structure (high level)
```
mlops-ds-interview-starter/
  configs/                 # YAML configs (no secrets)
  data/                    # synthetic generators + small samples
  sql/                     # analytics & engineering SQL
  fe/                      # feature contracts + builders
  ml/                      # evaluation, leakage, stability
  serving/                 # FastAPI app + Dockerfile + compose
  notebooks/               # (optional demos; add later)
  design/                  # architecture/runbooks/AB guide
  templates/               # interview templates (public-safe)
  scripts/                 # helper scripts
  tests/                   # unit tests
  .github/workflows/       # CI (no secrets in code)
```

## Safety checklist before pushing
- `.env` **not** committed; only `.env.example` exists
- No real names/domains/keys appear (search for `AKIA`, `SECRET`, `BEGIN RSA`, `@real-domain`)
- Generated plots and notebooks contain **no PII**


## Full stack (Docker Compose): API + MLflow + MinIO
```bash
# 0) Ensure Docker Desktop is running
# 1) Build & start full stack
make run-stack

# 2) Train & log to MLflow (another terminal)
MLFLOW_TRACKING_URI=http://localhost:5000 make train-local

# 3) Open UIs
# MinIO Console: http://localhost:9001  (user/pass: minioadmin/minioadmin)
# MLflow UI:     http://localhost:5000
# API Docs:      http://localhost:8000/docs

# 4) Optional: quick MLflow logging demo
make mlflow-demo
```
> Artifacts are stored in MinIO bucket `${MINIO_BUCKET:-mlflow}`; backend store is a local SQLite DB inside the mlflow container.
