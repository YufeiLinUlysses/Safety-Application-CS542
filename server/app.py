import json
from flask import Flask, jsonify
from Database.checkTables import checkTableExists
from Database.testDB import createTestTable, fetchAllFromGDP, insertGDPData
import pymysql
app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db="test",
    port=3306
)


@app.route('/gdp', methods=["GET"])
def index():
    result = fetchAllFromGDP(db)
    db.close()
    print(result)
    return result


app.run()

# print( json.dumps([
#         {"country": "USA", "value": 20.5},
#         {"country": "China", "value": 13.4},
#         {"country": "Germany", "value": 4.0},
#         {"country": "Japan", "value": 4.9},
#         {"country": "France", "value": 2.8}
#     ]))
