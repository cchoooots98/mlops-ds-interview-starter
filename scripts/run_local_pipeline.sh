#!/usr/bin/env bash
set -e
make data-sample
make train-local
make run-api
