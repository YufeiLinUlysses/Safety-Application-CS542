import json
from flask import Flask, jsonify
from Database.testDB import fetchAllFromGDP
from dbconnection import DB
import pymysql
app = Flask(__name__)

db = DB("CRIMINALANALYSIS").db

@app.route('/gdp', methods=["GET"])
def gdp():
    db = DB("test").db
    # createTestTable(db)
    # insertGDPData(db)
    # print(checkTableExists(db,'gdp'))
    result = fetchAllFromGDP(db)
    print(result)
    return result

if __name__ == "__main__":
    app.run(debug = True)
   
