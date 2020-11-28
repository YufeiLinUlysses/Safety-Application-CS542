import json
from flask import Flask, request
import datetime
from Database.dbconnection import DB
from Database import envir, involve, loc, person_file as pf, crime_file as cf, crime_type as ct, insert_table
import numpy as np
import ML.Model.train_test as TT

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


@app.route('/locCrimeCount', methods=['POST'])
def locCCnt():
    db = DB("CRIMINALANALYSIS")
    data = request.get_json()
    lat = float(data["lat"])
    lng = float(data["lng"])
    result = db.selectDB(cf.GetSql("CntCrime"), (lat, lng))
    return result


@app.route('/safetyindex', methods=['POST'])
def safetyindex():
    # DAY_OF_WEEK = {"MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3,
    #                "THURSDAY": 4, "FRIDAY": 5, "SATURDAY": 6, "SUNDAY": 7}
    data = request.get_json()
    W = np.mat([[0.70589358, 0.57894807, 0.57555195, 0.64646587, 0.45634837],
                [0.69749017, 0.56445017, 0.38924738, 0.67382041, 0.68272357],
                [0.67179093, 0.5696221, 0.65087029, 0.95102331, 0.32250566]])
    b = np.mat([[0.4704748],
                [0.83051006],
                [-0.48455419]])

    # X feature: MONTH, DAY_OF_WEEK, HOUR, LATITUDE-36, LONGTITUDE+78
    raw_input = np.array(
        [[data["month"], data["day"], data["hour"], data["lat"], data["lng"]]])
    # for i in range(0, raw_input.shape[0]):
    #     raw_input[i, 1] = DAY_OF_WEEK[raw_input[i, 1]]
    #     raw_input[i,3] = DISTRICT[raw_input[i,3]]
    input = np.mat(raw_input.astype(np.float))

    # z_score with mean, std from big data
    input = input.T
    mean = [6.581255, 3.9459, 13.29537, 42.322349287354555, -71.0826005364158]
    std = [3.275075209056275, 1.9669222633342682,
           6.271098513267034, 0.03175847257436829, 0.02939035430914813]
    for i in range(0, input.shape[0]):
        input[i] = (input[i]-mean[i])/std[i]
    input = input.T
    # print(input)

    Y, _ = TT.predict(input, W, b)
    return json.dumps({"SI": Y[0]})


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
