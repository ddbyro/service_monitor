#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
app = Flask(__name__)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

config = yaml.full_load(open('./config.yaml'))
hostnames = config['services']

#connection information to database, and Rev
def rev_mon(env):
   table = '{0}_servers'.format(env)
   hostnames = []
   #conn = sql.connect("database.db")
   #rows = conn.execute("select hostname from {0}".format(table))


   #generate list of hostnames
   for hostname in hostnames:
       if hostname['hostname'] == 'prod':
           hostname['hostname'].append(hostname[0])


   print(hostnames)

rev_mon(prod)