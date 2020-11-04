FROM python:3.9.0
ADD src/ .
RUN pip install -r requirements.txt
CMD ["python", "./service_monitor.py"]