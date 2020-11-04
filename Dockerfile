FROM python:3.9.0
RUN mkdir -p /opt/monitor
WORKDIR /opt/monitor
COPY src/ /opt/monitor
RUN pip install -r requirements.txt
CMD ["python", "service_monitor.py"]