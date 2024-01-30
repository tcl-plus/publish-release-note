FROM python:3.11.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app/
ENTRYPOINT ["python", "main.py"]
CMD ["--help"]
