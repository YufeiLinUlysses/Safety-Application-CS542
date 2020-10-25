import json
from flask import Flask
from Database.dbconnection import DB
from Database import envir, involve, loc, person_file as pf, crime_file as cf, crime_type as ct
app = Flask(__name__)


@app.route('/weathercnt', methods=["GET"])
def weathercnt():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("CntWeather"))
    return result


@app.route('/precipitation', methods=["GET"])
def precipitation():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("pM"))
    return result


@app.route('/temperature', methods=["GET"])
def temperature():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("tM"))
    return result


@app.route('/humidity', methods=["GET"])
def humidity():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("hM"))
    return result


@app.route('/windspeed', methods=["GET"])
def windSpeed():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("wsM"))
    return result


if __name__ == "__main__":
    app.run(debug=True)
