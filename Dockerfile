FROM python:3.9.12-slim


WORKDIR /app

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy project
COPY  backtester.py /app
COPY  smacross.py /app

# Instantiate database
ENTRYPOINT [ "python3", "/app/backtester.py" ]
