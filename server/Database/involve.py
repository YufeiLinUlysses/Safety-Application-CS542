import json
import csv

CREATE_SQL = {"CreateInvolve": "CREATE TABLE INVOLVE (pID INT, crimeID INT, IsVictim Char(1))"}

SELECT_SQL = {"SelectAll": "Select * from INVOLVE",
            "SelectByPIDcrimeID": "Select * from INVOLVE where pID = %s and crimeID = %s"
              }
INSERT_SQL = {"InsertALL": "INSERT INTO INVOLVEFILE VALUES(%s, %s, %s)" }
DROP_SQL = {"DropTable": "DROP TABLE INVOLVEFILE"}


def GetData():
    involveDataList = []
    with open('involve.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
            elif line_count > 300000: 
                break
            else:
                involveDataList.append((int(row[0]), int(row[1]), row[2])) # correspond to (pID INT, crimeID INT, IsVictim Char(1))
            line_count += 1

    return involveDataList

def CreateTable(dbcon):
    dbcur = dbcon.cursor()
    sql = CREATE_SQL["CreateInvolve"]
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

def SelectByPIDcrimeID(dbcon, pid, crimeID):
    sql = SELECT_SQL["SelectByPIDcrimeID"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql, pid, crimeID)
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
    involveData = GetData()
    print("involveData is", involveData)
    sql = INSERT_SQL["InsertALL"]
    try:
        dbcur = dbcon.cursor()
        dbcur.executemany(sql, involveData)
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

def TestCase(db, ipID=0, crimeID=0):
    CreateTable(db)
    InsertData(db)
    result = SelectAll(db)
    return result
    DropTable(db)
    return None