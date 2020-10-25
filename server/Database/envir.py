# Author: Yufei Lin
# Email: ylin9@wpi.edu
import json
import csv

CREATE_SQL = {"CreateEnv": '''CREATE TABLE ENVIRONMENT(
    WDATE INT,
    HOUR INT,
    TEMP INT,
    HUMIDITY INT,
    WINDSPEED INT,
    PRESSURE INT,
    VISIBILITY INT,
    SUNRISE INT,
    SUNSET INT,
    WEATHER VARCHAR(128),
    PRIMARY KEY(WDATE, HOUR))'''}

SELECT_SQL = {"SelectAll": "Select * from ENVIRONMENT",
              "CntWeather": '''(SELECT WEATHER AS text, COUNT(*) AS value 
                                FROM ENVIRONMENT 
                                GROUP BY WEATHER) 
                                ORDER BY value DESC''',
              "avgWS": '''SELECT 
                            MONTH(FROM_UNIXTIME(WDATE)) AS m, 
                            AVG(WINDSPEED) AS avgWS 
                          FROM ENVIRONMENT 
                          GROUP BY MONTH(FROM_UNIXTIME(WDATE))
              '''}
INSERT_SQL = {"InsertALL": '''INSERT INTO ENVIRONMENT VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''}


def GetData():
    with open('./Database/DataSource/Environment/bosFinal.csv') as f:
        f.readline()
        envData = [tuple(line) for line in csv.reader(f)]
    return envData


def CreateTable(dbcon):
    dbcur = dbcon.cursor()
    sql = CREATE_SQL["CreateEnv"]
    try:
        dbcur.execute(sql)
        sqlQuery = "show tables"
        dbcur.execute(sqlQuery)
        rows = dbcur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        dbcon.rollback()
        print("Exeception occured:{}".format(e))


def SelectAll(dbcon):
    sql = SELECT_SQL["SelectAll"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql)
        rows = dbcur.fetchall()
        columns = [desc[0] for desc in dbcur.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        final = json.dumps(result)
        return final
    except Exception as e:
        dbcon.rollback()
        print(e)
        return None


def InsertData(dbcon):
    envData = GetData()
    sql = INSERT_SQL["InsertALL"]
    try:
        dbcur = dbcon.cursor()
        dbcur.executemany(sql, envData)
        dbcon.commit()
    except Exception as e:
        print(e)


def cntWeather(dbcon):
    sql = SELECT_SQL["CntWeather"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql)
        rows = dbcur.fetchall()
        columns = [desc[0] for desc in dbcur.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        final = json.dumps(result)
        return final
    except Exception as e:
        print(e)
        return {"Error": e}


def avgWindSpeed(dbconn):
    sql = SELECT_SQL["avgWS"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql)
        rows = dbcur.fetchall()
        columns = [desc[0] for desc in dbcur.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        final = json.dumps(result)
        return final
    except Exception as e:
        print(e)
        return {"Error": e}
