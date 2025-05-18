FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir out
COPY . .
RUN pytest --cov-report html:out/cov_html --cov=. tests/ 
EXPOSE 5000
ENTRYPOINT FLASK_APP=file_uploader.py flask run --host=0.0.0.0 --port=5000
