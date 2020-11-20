import json
import csv
import os

PEOPLE_SQL = {"CreatePerson": "CREATE TABLE PERSONFILE (pid INT PRIMARY KEY, gender Char(1), BirthDate varchar(50), race varchar(55), tool varchar(25), Job Char(65))",
"SelectAll": "Select * from PERSONFILE",
"SelectByPID": "Select * from PERSONFILE where pid = %s",
"InsertALL": "INSERT ignore INTO PERSONFILE VALUES(%s, %s, %s, %s, %s, %s)" ,
"DropTable": "DROP TABLE IF EXISTS PERSONFILE",
"ColumnNumber": "SELECT COUNT(*) FROM PERSONFILE",
}

def GetData():
    personDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/Person/people.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue

            personDataList.append((int(row[0]), row[1], row[2], row[3], row[4], row[5])) # correspond to (pid INT, gender Char(1), BirthDate Date, race varchar(55), tool varchar(25), KnowsEachOther Char(1), Job Char(65))
            line_count += 1

    return personDataList

def GetSQL(sqlName):
    return PEOPLE_SQL[sqlName]
