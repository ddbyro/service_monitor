# from flask import Flask, render_template, request, redirect
# import sqlite3 as sql
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# app = Flask(__name__)
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import yaml

with open(r'./db.yaml') as file:
    services = yaml.load(file)
    print(services)

#connection information to database, and Rev
# def rev_mon(env):
#    table = '{0}_servers'.format(env)
#    hostnames= []
#    conn = sql.connect("database.db")
#    rows = conn.execute("select hostname from {0}".format(table))


   #generate list of hostnames
#    for row in rows:
#        hostnames.append(row[0])


#    for hostname in hostnames:
#        try:
#            #build out url for getting the version for all three brands
#            if (hostname[:3] == 'lx-') or (hostname[:3] == 'cr-'):
#                web_service = 'RevWebServices'
#            elif hostname[:3] == 'pgx':
#                web_service = 'ProgrexionServicesWeb'
#            rev_version = requests.get('http://{0}:8080/{1}/resources/systemUtils/version'.format(hostname,web_service), timeout=5)
#            #get version information from above check
#            if rev_version.status_code == requests.codes.ok:
#                version = rev_version.text
#            else:
#                version = "Status: {0}".format(rev_version.status_code)
#        except:
#            version = "Check Failed (Wildfly might be down)"


#        try:
#            #same thing as above but for the testMode column for all three brands
#            if (hostname[:3] == 'lx-') or (hostname[:3] == 'cr-'):
#                web_service = 'RevWebServices'
#            elif hostname[:3] == 'pgx':
#                web_service = 'ProgrexionServicesWeb'
#            testmode = requests.get('http://{0}:8080/{1}/resources/systemUtils/isTestMode'.format(hostname,web_service), timeout=5)
#            #get version information from above check
#            if testmode.status_code == requests.codes.ok:
#                test_mode = testmode.text
#            else:
#                test_mode = "Status: {0}".format(testmode.status_code)
#        except:
#            test_mode = "Server Mode Check - Failed"


#        try:
#            # this is for the isAlive check column for all three brands
#            rev_isalive = requests.get('http://{0}:8080/{1}/resources/systemUtils/isAlive'.format(hostname,web_service), timeout=5)
#            if rev_isalive.text == 'true':
#                status_color = 'green'
#            else:
#                status_color = 'red'
#        except:
#            status_color = 'red'
#        print ('{0}, {1}, {2}, {3}, {4}'.format(table, version, status_color, test_mode, hostname)) #prints off information populated that will be used in the database update
#        conn.execute("UPDATE {0} SET version='{1}', service_status='{2}', test_mode='{3}' WHERE hostname='{4}'".format(table, version, status_color,test_mode, hostname)) #executes database update
#        conn.commit()


#        conn.row_factory = sql.Row #this allows you to return an object that can also access columns by name
#        curr = conn.cursor() #creates the cursor
#        curr.execute("select * from {0} order by environment DESC, hostname ASC".format(table)) #this will execute the select statement against the database using the cursor
#        rows = curr.fetchall(); #returns a list of all rows from the select statement that you ran above


#    return render_template('rev.html',rows = rows)


# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/rev')
# def rev():
#     return rev_mon('prod')


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