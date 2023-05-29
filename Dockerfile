FROM python:3.10

COPY requirements.txt /app/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
COPY . /app/

CMD ["python3.10", "app.py"]
