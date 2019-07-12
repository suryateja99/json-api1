from flask import Flask
from flask_mysqldb import MySQL
import json
from flask import jsonify



app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Ace@3915'
app.config['MYSQL_DB']='dash_board'
mysql = MySQL(app)
@app.route("/")

def hello():

    cur = mysql.connection.cursor()

    cur.execute('''select * from breach''')
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)
    









if __name__ == "__main__":

       app.run(debug=1)
