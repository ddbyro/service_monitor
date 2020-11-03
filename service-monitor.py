from flask import Flask, render_template, request, redirect
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
app = Flask(__name__)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import yaml

config = yaml.full_load(open('./config.yaml'))
hostnames = config['services']

#connection information to database, and Rev
def rev_mon(env):
   table = '{0}_servers'.format(env)
   hostnames= []
   rows = len(hostname)
#    conn = sql.connect("database.db")
#    rows = conn.execute("select hostname from {0}".format(table))


   #generate list of hostnames
   for hostname in hostnames:
       if hostname['environment'] == "prod":
           hostnames.append(hostname['hostname'])

       try:
           # this is for the isAlive check column for all three brands
           rev_isalive = requests.get('http://{0}:8080/{1}/resources/systemUtils/isAlive'.format(hostname,web_service), timeout=5)
           if rev_isalive.text == 'true':
               status_color = 'green'
           else:
               status_color = 'red'
       except:
           status_color = 'red'


   return render_template('rev.html',rows = rows)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/rev')
def rev():
    return rev_mon('prod')


# @app.route('/rev_dev')
# def rev_dev():
#    return rev_mon('dev')


# @app.route('/rev_test')
# def rev_test():
#    return rev_mon('test')




# @app.route('/rev_stage')
# def rev_stage():
#    return rev_mon('stage')




# if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5002, debug = True)