FROM python:3.9.0
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
ADD static/ .
ADD templates/ .
COPY service-monitor.py .
CMD ["python", "./service_monitor.py"]