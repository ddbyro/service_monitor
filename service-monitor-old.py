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

urls = []

for hostname in hostnames:
    if hostname['environment'] == "prod":
        urls.append(hostname['hostname'])

print(urls)
#connection information to database, and Rev
# def rev_mon(env):
#    #table = '{0}_servers'.format(env)
#    urls = []
#    #conn = sql.connect("database.db")
#    #rows = conn.execute("select hostname from {0}".format(table))


#    #generate list of hostnames
#    for hostname in hostnames:
#        if hostname['environment'] == 'prod':
#            hostname['hostname'].append(urls[0])


#    print(urls)

# rev_mon('prod')