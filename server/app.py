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
    # createTestTable(db)
    # insertGDPData(db)
    # print(checkTableExists(db,'gdp'))
    result = fetchAllFromGDP(db)
    print(result)
    return result


app.run()
