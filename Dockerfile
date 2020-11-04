FROM python:3.9.0
COPY src/ .
RUN pip install -r requirements.txt
CMD ["python", "service_monitor.py"]