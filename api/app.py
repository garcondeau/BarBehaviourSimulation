from flask import Flask, render_template, url_for
import pyodbc

app = Flask(__name__)


print("===================================================================")
server = '127.0.0.1'
database = 'BarBehaviourSimulation'
username = 'sa'
password = '75Bky%mN7R'
print("connecting.......")
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=172.44.0.8,1433;DATABASE=BarBehaviourSimulation;ENCRYPT=yes;UID=sa;PWD=75Bky%mN7R;TrustServerCertificate=yes;Connection Timeout=30;')
cursor = cnxn.cursor()
print("connected!")
print("==================================================================")

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='172.44.0.3')
