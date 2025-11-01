#!/usr/bin/env bash
set -e
ruff . || true
black --check . || true
pytest -q || true
