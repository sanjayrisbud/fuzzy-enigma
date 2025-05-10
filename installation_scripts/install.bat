python -m venv venv
venv\Scripts\activate.bat & pip install -r requirements.txt & pytest --cov-report html:tests/cov_html --cov=. tests/ & python file_uploader.py
