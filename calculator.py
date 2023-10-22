from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='calculate'
)
cursor = con.cursor()

@app.route('/get_history', methods=['POST'])
def get_history():
    data = request.get_json()
    calculation = data.get('calculation')
    result = data.get('result')

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (time, calculation, result)
    insert = "INSERT INTO app1_calculation VALUES (%s, %s, %s)"
    cursor.execute(insert, data)
    con.commit()

    response_message = "ok"
    return jsonify({"message": response_message})

@app.route('/get_calculation', methods=['GET'])
def get_calculation():
    cursor.execute("SELECT calculation, result FROM app1_calculation ORDER BY time DESC LIMIT 10")
    data = cursor.fetchall()
    return jsonify({"data": data})

if __name__ == '__main__':
    app.run(debug=True)
