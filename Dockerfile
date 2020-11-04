FROM python:slim-buster
RUN mkdir -p /opt/monitor
WORKDIR /opt/code
COPY . /opt/code
RUN pip install -r requirements.txt
CMD ["python", "service_monitor.py"]