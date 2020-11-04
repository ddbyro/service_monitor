#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import yaml
app = Flask(__name__)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

config = yaml.full_load(open('./config/config.yaml'))
hostnames = config['services']

def service_mon(env):
   service_info = []

   for hostname in config['services']:
       #test_mode = "Status: {0}".format('false')
       try:
           service_isalive = requests.get('{0}'.format(hostname['hostname']), timeout=5)

           if service_isalive.status_code == requests.codes.ok:
               status_color = 'green'
               service_info.append({'name':hostname['name'],'hostname':hostname['hostname'],'environment':hostname['environment'],'version':hostname['version'],'status_color': status_color})
           else:
               status_color = 'red'
               service_info.append({'name':hostname['name'],'hostname':hostname['hostname'],'environment':hostname['environment'],'version':hostname['version'],'status_color': status_color})
       except:
           status_color = 'red'
           service_info.update({'name':hostname['name'],'hostname':hostname['hostname'],'environment':hostname['environment'],'version':hostname['version'],'status_color': status_color})
           #print '{0}_servers, {1}, {2}, {3}, {4}'.format(service_info['host_status']['environment'], service_info['host_status']['version'], service_info['host_status']['status_color'], test_mode, service_info['host_status']['hostname']) #prints off information populated that will be used in the database update
   #return service_info
   return render_template('service01.html',service_info = service_info)

#print(service_mon('prod'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/service01')
def service():
    return service_mon('prod')


@app.route('/rev_dev')
def rev_dev():
   return rev_mon('dev')


@app.route('/rev_test')
def rev_test():
   return rev_mon('test')


@app.route('/rev_stage')
def rev_stage():
   return rev_mon('stage')




if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5002, debug = True)

