FROM python:3.9.0
COPY . /app
WORKDIR /app
EXPOSE 5002
CMD ["python", "./service_monitor.py"]