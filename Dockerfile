FROM python:3.9.0-slim
WORKDIR /usr/src/app
COPY . /usr/src/app
EXPOSE 5002
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["python", "service-monitor.py"]