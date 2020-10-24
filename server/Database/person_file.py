import json
import csv

CREATE_SQL = {"CreatePerson": "CREATE TABLE PERSONFILE (pid INT, gender Char(1), BirthDate Date, race varchar(55), tool varchar(25), KnowsEachOther Char(1), Job Char(65))"}

SELECT_SQL = {"SelectAll": "Select * from PERSONFILE",
            "SelectByPID": "Select * from PERSONFILE where pid = %s"
              }
INSERT_SQL = {"InsertALL": "INSERT INTO PERSONFILE VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" }
DROP_SQL = {"DropTable": "DROP TABLE PERSONFILE"}

def GetData():
    personDataList = []
    with open('person.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
            elif line_count > 300000:
                break
            else:
                personDataList.append((int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])) # correspond to (pid INT, gender Char(1), BirthDate Date, race varchar(55), tool varchar(25), KnowsEachOther Char(1), Job Char(65))
            line_count += 1

    return personDataList

def CreateTable(dbcon):
    dbcur = dbcon.cursor()
    sql = CREATE_SQL["CreatePerson"]
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

def SelectByPID(dbcon, pid):
    sql = SELECT_SQL["SelectByPID"]
    try:
        dbcur = dbcon.cursor()
        dbcur.execute(sql, pid)
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
    personData = GetData()
    print("personData is", personData)
    sql = INSERT_SQL["InsertALL"]
    try:
        dbcur = dbcon.cursor()
        dbcur.executemany(sql, personData)
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

def TestCase(db, iPID=0):
    CreateTable(db)
    InsertData(db)
    result = SelectAll(db)
    return result
    DropTable(db)
    return None