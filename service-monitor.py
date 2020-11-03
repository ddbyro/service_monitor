from flask import Flask, render_template, request, redirect
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
app = Flask(__name__)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import yaml

config = yaml.full_load(open('./config.yaml'))

#connection information to database, and Rev
def service_mon(env):
   hostnames = []

   #generate list of hostnames
   for hostname in config['services']:
       if hostname['environment'] == "prod":
           hostnames.append(hostname['hostname'])

       try:
           # this is for the isAlive check column for all three brands
           service_isalive = requests.get('{0}'.format(hostname['hostname']), timeout=5)
           if service_isalive.text == 'true':
               status_color = 'green'
           else:
               status_color = 'red'
       except:
           status_color = 'red'


   return render_template('service01.html',rows = hostnames)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/service01')
def rev():
    return service_mon('prod')


# @app.route('/rev_dev')
# def rev_dev():
#    return rev_mon('dev')


# @app.route('/rev_test')
# def rev_test():
#    return rev_mon('test')




# @app.route('/rev_stage')
# def rev_stage():
#    return rev_mon('stage')




if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5002, debug = True)