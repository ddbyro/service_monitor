FROM python:3.9.0
COPY . /app
WORKDIR /app
EXPOSE 5002
CMD ["python2", "service_monitor.py"]