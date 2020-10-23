import json
from flask import Flask, jsonify
from Database.checkDatabase import createDatabase
from Database.testDB import insertGDPData
import pymysql
app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db="CRIMINALANALYSIS",
    port=3306
)



@app.route('/gdp', methods=["GET"])
def gdp():
    # createTestTable(db)
    # insertGDPData(db)
    # print(checkTableExists(db,'gdp'))
    result = fetchAllFromGDP(db)
    return result

if __name__ == "__main__":
    app.run(debug = True)
   
