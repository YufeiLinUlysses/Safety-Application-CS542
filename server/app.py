import json
from flask import Flask
from Database.testDB import fetchAllFromGDP
from Database.dbconnection import DB
from Database import envir, involve, loc, person_file as pf, crime_file as cf, crime_type as ct
app = Flask(__name__)

db = DB("CRIMINALANALYSIS")


@app.route('/gdp', methods=["GET"])
def gdp():
    db = DB("test").db
    result = fetchAllFromGDP(db)
    return result


@app.route('/weathercnt', methods=["GET"])
def weathercnt():
    result = db.selectDB(envir.GetSQL("CntWeather"))
    return result


@app.route('/precipitation', methods=["GET"])
def precipitation():
    result = db.selectDB(envir.GetSQL("pM"))
    return result


@app.route('/tM', methods=["GET"])
def temperature():
    result = db.selectDB(envir.GetSQL("tM"))
    return result


@app.route('/humidity', methods=["GET"])
def humidity():
    result = db.selectDB(envir.GetSQL("hM"))
    return result


@app.route('/windspeed', methods=["GET"])
def windSpeed():
    result = db.selectDB(envir.GetSQL("wsM"))
    return result


if __name__ == "__main__":
    app.run(debug=True)
