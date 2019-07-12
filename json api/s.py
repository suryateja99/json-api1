from flask import Flask
from flask_mysqldb import MySQL
import json


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Ace@3915'
app.config['MYSQL_DB']='dash_board'
mysql = MySQL(app)

@app.route("/")
def hello():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM botstat''')
    result = cur.fetchall()
    return json.dumps(result)




if __name__ == "__main__":
       app.run(debug=1)
 