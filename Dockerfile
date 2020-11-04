FROM python:slim-buster
RUN mkdir -p /opt/monitor
WORKDIR /opt/code
ADD . /opt/code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]