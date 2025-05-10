#!/bin/bash
python3 -m venv venv
source venv/bin/activate && pip install -r requirements.txt && pytest --cov-report html:tests/cov_html --cov=. tests/ && python file_uploader.py
