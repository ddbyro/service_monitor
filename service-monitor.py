#!/usr/bin/env python3.9
from flask import Flask, render_template
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import yaml

app = Flask(__name__)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

config = yaml.full_load(open('./config/config.yaml'))



def service_mon(service_env):
    hostnames = config[f'{service_env}_services']
    service_info = []

    for hostname in hostnames:
        try:
            service_isalive = requests.get(f'{hostname["hostname"]}', verify=False, timeout=5)

            if service_isalive.status_code == requests.codes.ok:
                status_color = 'green'
                service_info.append(
                    {'name': hostname['name'],
                     'hostname': hostname['hostname'],
                     'environment': hostname['environment'],
                     'version': hostname['version'],
                     'status_color': status_color})

            else:
                status_color = 'red'
                service_info.append(
                    {'name': hostname['name'],
                     'hostname': hostname['hostname'],
                     'environment': hostname['environment'],
                     'version': hostname['version'],
                     'status_color': status_color}
                )

        except:
            status_color = 'red'
            service_info.append(
                {'name': hostname['name'],
                 'hostname': hostname['hostname'],
                 'environment': hostname['environment'],
                 'version': hostname['version'],
                 'status_color': status_color}
            )

    return render_template(f'service_mon_{service_env}.html', service_info=service_info)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/service_mon_prod')
def service():
    return service_mon('prod')


@app.route('/service_mon_dev')
def service_dev():
    return service_mon('dev')


@app.route('/service_mon_stage')
def service_stage():
    return service_mon('stage')


def main():
    app.run(host='0.0.0.0', port=5002, debug=True)


if __name__ == '__main__':
    main()
