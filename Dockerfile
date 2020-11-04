FROM python:3.7.5-slim
WORKDIR /usr/src/app
COPY . /usr/src/app
EXPOSE 5002
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["python", "service-monitor.py"]