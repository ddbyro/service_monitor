FROM python:3.9.0
COPY . /app
WORKDIR /app
EXPOSE 5002
RUN pip install pyyaml flask rewuests
CMD ["python", "service_monitor.py"]
#CMD ["watch", "ls"]