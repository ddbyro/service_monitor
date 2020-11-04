FROM python:3.9.0
WORKDIR /usr/src/app
COPY . /usr/src/app
EXPOSE 5002
RUN python -m pip install pyyaml flask requests
CMD ["python", "service_monitor.py"]
#CMD ["watch", "whoami"]