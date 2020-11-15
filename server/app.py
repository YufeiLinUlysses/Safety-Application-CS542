import json
from flask import Flask, request
from Database.dbconnection import DB
from Database import envir, involve, loc, person_file as pf, crime_file as cf, crime_type as ct
import data_manager
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


@app.route('/location', methods=["GET"])
def location():
	db = DB("CRIMINALANALYSIS")
	result = db.selectDB(loc.GetSQL('SelectLocation'))
	return result


@app.route('/street', methods=['GET'])
def street():
	db = DB('CRIMINALANALYSIS')
	result = db.selectDB(loc.GetSQL('streetCount'))
	return result


@app.route('/district', methods=['GET'])
def district():
	db = DB('CRIMINALANALYSIS')
	result = db.selectDB(loc.GetSQL('districtCount'))
	return result


@app.route('/weatherCrime', methods=['GET'])
def weaCr():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("wC"))
    return result

@app.route('/humCrime', methods=['GET'])
def humCr():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("hC"))
    return result


@app.route('/tempCrime', methods=['GET'])
def tempCr():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("tC"))
    return result

@app.route('/crimeLocAnalysize', methods=['GET'])
def cla():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("tC"))
    return result


@app.route('/getCrimeByLoc', methods=['POST'])
def GetCrime():
    requestData = request.get_json()
    fLat = float(requestData.get("lat"))
    fLon = float(requestData.get("lon"))
    result = data_manager.GetCrimeFileByLoc(fLat, fLon)
    return result



# if __name__ == "__main__":
app.run(debug=True)
