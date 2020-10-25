import json
import csv
import os
CREATE_SQL = {"CreatePerson": "CREATE TABLE PERSONFILE (pid INT, gender Char(1), BirthDate Date, race varchar(55), tool varchar(25), KnowsEachOther Char(1), Job Char(65))"}

SELECT_SQL = {"SelectAll": "Select * from PERSONFILE",
            "SelectByPID": "Select * from PERSONFILE where pid = %s"
              }
INSERT_SQL = {"InsertALL": "INSERT INTO PERSONFILE VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" }
DROP_SQL = {"DropTable": "DROP TABLE PERSONFILE"}

PEOPLE_SQL = {"CreatePerson": "CREATE TABLE PERSONFILE (pid INT PRIMARY KEY, gender Char(1), BirthDate varchar(50), race varchar(55), tool varchar(25), KnowsEachOther Char(1), Job Char(65))",
"SelectAll": "Select * from PERSONFILE",
            "SelectByPID": "Select * from PERSONFILE where pid = %s",
"InsertALL": "INSERT INTO PERSONFILE VALUES(%s, %s, %s, %s, %s, %s, %s)" ,
"DropTable": "DROP TABLE IF EXISTS PERSONFILE",

}

def GetData():
    personDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/Person/person.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
            elif line_count > 7:
                break
            else:
                personDataList.append((int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])) # correspond to (pid INT, gender Char(1), BirthDate Date, race varchar(55), tool varchar(25), KnowsEachOther Char(1), Job Char(65))
            line_count += 1

    return personDataList

def GetSQL(sqlName):
    return PEOPLE_SQL[sqlName]
