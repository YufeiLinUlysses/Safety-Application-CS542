import json
from flask import Flask, request
from Database.dbconnection import DB
from Database import envir, involve, loc, person_file as pf, crime_file as cf, crime_type as ct, insert_table
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


@app.route('/wsCrime', methods=['GET'])
def wsCr():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("wsC"))
    return result


@app.route('/preCrime', methods=['GET'])
def pCr():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("pC"))
    return result


@app.route('/crimeLocAnalysize', methods=['GET'])
def cla():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(envir.GetSQL("tC"))
    return result


@app.route('/typecnt', methods=['GET'])
def typecnt():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(ct.GetSQL("typecnt"))
    return result


@app.route('/locAnalysis', methods=['POST'])
def locAna():
    db = DB("CRIMINALANALYSIS")
    data = request.get_json()
    print(data)
    lat = float(data["lat"])
    lng = float(data["lng"])
    print(lat)
    print(lng)
    result = db.selectDB(cf.GetSql("SelectCrimeByLoc"), (lat, lng, lat, lng))
    print(result)
    return result


@app.route('/insertCrime', methods=['POST'])
def Insert2Insert():
    db = DB("CRIMINALANALYSIS")
    insertData = request.get_json()
    sName = insertData.get("name")
    sNameState = insertData.get("nameState")
    sCriminal = insertData.get("criminal")
    sVictim = insertData.get("victim")
    sRelation = insertData.get("relation")
    sType = insertData.get("type")
    sName = insertData.get("name")
    sLat = insertData.get("latitude")
    sLon = insertData.get("longitude")
    sTime = insertData.get("ctime")
    sDate = insertData.get("cdate")
    insertData = ((sName, sNameState, sCriminal, sVictim,
                   sRelation, sType, sName, sLat, sLon, sTime, sDate))
    db.insertDB(insert_table.GetSql("INSERT_SQL"), insertData)
    return 1


# if __name__ == "__main__":
app.run(debug=True)
