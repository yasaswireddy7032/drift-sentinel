# Drift Sentinel

[![Tests](https://github.com/yasaswireddy7032/drift-sentinel/actions/workflows/tests.yml/badge.svg)](https://github.com/yasaswireddy7032/drift-sentinel/actions)

Distribution monitoring with fixed reference bins, population stability index, and explicit missing-data checks.

**Status:** runnable portfolio reference implementation. Uses synthetic or hand-authored demonstration data. No employer code, customer data, or production performance claims.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
python -m unittest -v
```

The default command prints a reproducible JSON demonstration. See `app.py` for the reusable Python API. `example-output.json` records the locally executed demo; it is not an external benchmark.

## Architecture

Reference sample → frozen quantile boundaries → smoothed distributions → PSI + missingness → investigation signal. All boundaries and distributions are included in the report for audit.

## Validation

Tests exercise failure cases and behavioral invariants, in addition to the executable demo. GitHub Actions runs the tests and demo on pushes and pull requests. See the Actions tab for current results.

## Limitations and next steps

PSI thresholds are illustrative heuristics, not significance tests. Feature drift is not proof of performance drift. Add minimum sample rules, multiple-feature correction, delayed-label metrics, and alert deduplication before operational monitoring.

## Container

```bash
docker build -t drift-sentinel .
docker run --rm drift-sentinel
```

The Docker recipe is provided; local validation uses Python, not Docker.

## Responsible use

Review the code and understand its assumptions before deploying. Keep credentials in environment variables and exclude private data from commits. This project is an educational engineering baseline, not a production-certified service.
