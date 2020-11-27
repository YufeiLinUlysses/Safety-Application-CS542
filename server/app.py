import json
from flask import Flask, request
import datetime
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
    lat = float(data["lat"])
    lng = float(data["lng"])
    result = db.selectDB(cf.GetSql("SelectCrimeByLoc"), (lat, lng, lat, lng))
    return result


@app.route('/locTimeCount', methods=["POST"])
def locTCount():
    db = DB("CRIMINALANALYSIS")
    data = request.get_json()
    lat = float(data["lat"])
    lng = float(data["lng"])
    result = db.selectDB(cf.GetSql("TimeslotCount"), (lat, lng))
    return result


@app.route('/locPDCount', methods=["POST"])
def pDCount():
    db = DB("CRIMINALANALYSIS")
    data = request.get_json()
    lat = float(data["lat"])
    lng = float(data["lng"])
    result = db.selectDB(cf.GetSql("PoliceDCount"), (lat, lng))
    return result


@app.route("/pds", methods=["GET"])
def pds():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(loc.GetSQL("PoliceDs"))
    return result


@app.route("/ctypes", methods=["GET"])
def ctypes():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(ct.GetSQL("SelectAllTypes"))
    return result

@app.route('/locCTypeCount', methods=["POST"])
def cTypeCount():
    db = DB("CRIMINALANALYSIS")
    data = request.get_json()
    lat = float(data["lat"])
    lng = float(data["lng"])
    result = db.selectDB(cf.GetSql("CTypeCount"), (lat, lng))
    return result


@app.route('/insertCrime', methods=['POST'])
def Insert2Insert():
    db = DB("CRIMINALANALYSIS")
    insertData = request.get_json()
    lat = insertData.get("Latitude")
    lng = insertData.get("Longitude")
    cDate = insertData.get("Date")
    cTime = insertData.get("Time")
    relation = insertData.get("Relation")
    criminal = insertData.get("Criminal")
    victim = insertData.get("Victim")
    ctype = insertData.get("Type")
    policeDistrict = insertData.get("PoliceDistrict")
    dt = datetime.datetime.strptime(cDate, '%Y-%m-%d')
    dt = dt.timestamp()

    insertData = [(lat, lng, dt, cTime, relation, criminal,
                   victim, ctype, policeDistrict)]
    iBefore = db.selectDB(insert_table.GetSql("TABLE_COUNT"))
    db.insertByOneDB(insert_table.GetSql("INSERT_SQL"), insertData)
    iAfter = db.selectDB(insert_table.GetSql("TABLE_COUNT"))
    if iAfter > iBefore:
        return json.dumps({"success": True})
    else:
        return json.dumps({"success": False})


@app.route('/requestInsert', methods=['GET'])
def RequestInsert():
    db = DB("CRIMINALANALYSIS")
    result = db.selectDB(insert_table.GetSql("SELECT_ALL"))
    return result


@app.route('/crimeConfirm', methods=['POST'])
def ConfirmRequest():
    db = DB("CRIMINALANALYSIS")
    confirmData = request.get_json()
    print(confirmData)
    for i in confirmData:
        queryID = i["ID"]
        conf = i["Confirmed"]
        db.updataDB(insert_table.GetSql("UPDATE_TABLE"), (conf, queryID))
    CrimeID = db.selectDB(cf.GetSql("SelectMAXID"))
    CrimeIDList = json.loads(CrimeID)
    iCrimeID = int(CrimeIDList[0].get('max(CRIMEID)')) + 1
    db.InsertWithErrorMessage(cf.GetSql("InsertFromInsertion"), [(iCrimeID)])
    db.InsertWithErrorMessage(cf.GetSql("InsertCrimePeople"))
    db.InsertWithErrorMessage(cf.GetSql("InsertVictimPeople"))
    db.InsertWithErrorMessage(cf.GetSql("InsertInvolve"), [(iCrimeID)])
    db.InsertWithErrorMessage(cf.GetSql("InsertInvolveCrime"), [(iCrimeID)])
    db.InsertWithErrorMessage(cf.GetSql("InsertRelation"))
    db.InsertWithErrorMessage(cf.GetSql("InsertCrimePeople"))
    db.DeletetDB(insert_table.GetSql("DELETE_CONFIRM"))

    return db.selectDB(insert_table.GetSql("SELECT_ALL"))


# if __name__ == "__main__":
app.run(debug=True)
