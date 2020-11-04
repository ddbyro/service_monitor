FROM python:slim-buster
RUN mkdir -p /opt/monitor
WORKDIR /opt/monitor
COPY src/ . 
RUN pip install -r requirements.txt
CMD ["python", "service_monitor.py"]