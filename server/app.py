import json
from flask import Flask, jsonify
from Database.checkTables import checkTableExists
from Database.createTables import createTestTable
from Database.fetchResult import fetchAllFromGDP
from Database.insertData import insertGDPData
import pymysql
app = Flask(__name__)

db = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "123456", 
        db = "test",
       port = 3306
    )

# print(checkTableExists(db, "gdp"))
createTestTable(db)
insertGDPData(db)
fetchAllFromGDP(db)
db.close()

# @app.route('/gdp', methods=["GET"])
# def index():
#     cursor = db.cursor()
#     cursor.execute("SELECT VERSION()")
#     data = cursor.fetchone()
#     print ("Database version : %s " % data)
#     db.close()
#     return json.dumps([
#         {"country": "USA", "value": 20.5},
#         {"country": "China", "value": 13.4},
#         {"country": "Germany", "value": 4.0},
#         {"country": "Japan", "value": 4.9},
#         {"country": "France", "value": 2.8}
#     ])

# app.run()
