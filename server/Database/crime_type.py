import json
import csv

CREATE_SQL = {"CreateCrimeType": "CREATE TABLE CRIMETYPE (TYPEID INT primary key, TYPEGROUP varchar(255) not null, DESCRIPTION varchar(255), SHOOTING char(1) default 'N')"}
SELECT_SQL = {"SelectAllCrimeType": "Select * from CRIMETYPE",
              "SelectCrimeTypeByCrimeID": "Select * from CRIMETYPE where TYPEID = %s"
              }
INSERT_SQL = {"InsertALL2CrimeType": "INSERT INTO CRIMETYPE VALUES(%s, %s, %s, %s)"}
DROP_SQL = {"DropCrimeType": "DROP TABLE CRIMETYPE"}
DELETE_SQL = {"DeleteCrimeType": "DELETE FROM CRIMETYPE WHERE TYPEID = %s"}

def GetData():
    crimeDataList = []
    with open('crime.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
            elif line_count > 3:
                break
            else:
                crimeDataList.append((line_count, "peopleName", row[13], int(row[1]), int(row[8])))
            line_count += 1

    return crimeDataList

def CreateTable(dbcon):
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


def TestCase(db, iCrimeID=0):
    CreateTable(db)
    InsertData(db)
    result = SelectAll(db)
    #result = SelectByID(db, iCrimeID)
    return result
