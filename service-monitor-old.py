#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import yaml
app = Flask(__name__)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

config = yaml.full_load(open('./config.yaml'))
hostnames = config['services']


#connection information to database, and Rev
def rev_mon(env):
#    table = '{0}_servers'.format(env)
#    hostnames= []
#    conn = sql.connect("database.db")
#    rows = conn.execute("select hostname from {0}".format(table))


   #generate list of hostnames
#    for hostname in config['services']:
#        hostnames.append(hostname['hostname'])


   for hostname in config['services']:
       test_mode = "Status: {0}".format('false')
       servive_info = {}    
       servive_info.update({'environment': hostname['environment'],'hostname': hostname['hostname'], 'version': hostname['version']})
       try:
           service_isalive = requests.get('{0}'.format(hostname['hostname']), timeout=5)

           if service_isalive.status_code == requests.codes.ok:
               status_color = 'green'
               servive_info.update({'status_color': 'green'})
           else:
               status_color = 'red'
               servive_info.update({'status_color': 'red'})

       except:
           status_color = 'red'
       print '{0}_servers, {1}, {2}, {3}, {4}'.format(hostname['environment'], hostname['version'], status_color, test_mode, hostname['hostname']) #prints off information populated that will be used in the database update

   return render_template('service01.html',hostnames = hostnames, status_color = status_color)
   #return rows

#print(rev_mon('prod'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/service01')
def rev():
    return rev_mon('prod')


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
