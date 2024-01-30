FROM python:3.11.6
RUN pip install -r requirements.txt
COPY . /app/
WORKDIR /app
ENTRYPOINT ["python", "main.py"]
CMD ["--help"]