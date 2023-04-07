import mysql.connector
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password = "kingghidorah1:)",
    name= "something"
)
print(mydb)

mycursor = mydb.cursor()

@app.route('/users', methods=['GET', 'POST'])

def users():

    if request.method == 'GET':
            serial_number = request.json['id']
            data = mycursor.execute("SELECT * FROM todolist WHERE Serial_Number=", (serial_number))
            print(data)
            return jsonify(data)

    elif request.method == 'POST':

            serial_number = request.json['id']
            task = request.json['task']
            status = request.json['status']
            mycursor.execute('INSERT INTO todolist (serial_number, task, status) VALUES (%s, %s, %s)', (serial_number, task, status))
            mydb.commit()
            return jsonify({'message': 'task created'})

if(__name__ == "__main__"):
    app.run()