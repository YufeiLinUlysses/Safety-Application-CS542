# Author: Torres Fan
# Email: xfan3@wpi.edu

import json
import csv
import checkTables

CREATE_SQL = {"CreateCrime": "CREATE TABLE CRIMEFILE (CRIMEID INT, PEOPLEID varchar(32), LOCATIONID varchar(32), TYPEID INT, TIME INT)"}
SELECT_SQL = {"SelectAll": "Select * from CRIMEFILE",
            "SelectByID": "Select * from CRIMEFILE where CRIMEID = %s"
              }
INSERT_SQL = {"InsertALL": "INSERT INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s)" }
DROP_SQL = {"DropTable": "DROP TABLE CRIMEFILE"}


def GetData():
    crimeDataList = []
    with open('crime.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            crimeDataList.append((line_count, "peopleName", row[13], int(row[1]), int(row[8])))
            line_count += 1

    return crimeDataList

def CreateTable(dbcon):
    if checkTables.checkTableExists(dbcon, "CRIMEFILE"):
        print("table already exists")
        return
    dbcur = dbcon.cursor()
    sql = CREATE_SQL["CreateCrime"]

    try:
        dbcur.execute(sql)
        sqlQuery = "show tables"
        dbcur.execute(sqlQuery)
        rows = dbcur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
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
        print(e)
        return None

def SelectByID(dbcon, crimeID):
    sql = SELECT_SQL["SelectByID"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql, crimeID)
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
        return None


def InsertData(dbcon):
    crimeData = GetData()
    print("crimeData is", crimeData)
    sql = INSERT_SQL["InsertALL"]
    try:
        dbcur = dbcon.cursor()
        dbcur.executemany(sql, crimeData)
        dbcon.commit()
    except Exception as e:
        print(e)

def DropTable(dbcon):
    sql = DROP_SQL["DropTable"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql)

    except Exception as e:
        print(e)
        return None


def TestCase(db, iCrimeID=0):
    # CreateTable(db)
    # InsertData(db)
    # result = SelectAll(db)
    # #result = SelectByID(db, iCrimeID)
    # return result
    DropTable(db)
    return None


def GetSql():
    pass

