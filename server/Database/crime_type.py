import json
import csv
import os


CREATE_SQL = {"CreateCrimeType": "CREATE TABLE CRIMETYPE (TYPEID INT primary key, TYPEGROUP varchar(255) not null, DESCRIPTION varchar(255), SHOOTING char(1) default 'N')"}
SELECT_SQL = {"SelectAllCrimeType": "Select * from CRIMETYPE",
              "SelectCrimeTypeByCrimeID": "Select * from CRIMETYPE where TYPEID = %s"
              }
INSERT_SQL = {"InsertALL2CrimeType": "INSERT INTO CRIMETYPE VALUES(%s, %s, %s, %s)"}
DROP_SQL = {"DropCrimeType": "DROP TABLE CRIMETYPE"}
DELETE_SQL = {"DeleteCrimeType": "DELETE FROM CRIMETYPE WHERE TYPEID = %s"}


CRIME_TYPE_SQL = {"CreateCrimeType": "CREATE TABLE CRIMETYPE (TYPEID INT primary key, DESCRIPTION varchar(255), SHOOTING char(1) default 'N')",
                  "SelectAllCrimeType": "Select * from CRIMETYPE",
                  "SelectCrimeTypeByCrimeID": "Select * from CRIMETYPE where TYPEID = %s",
                    "InsertALL2CrimeType": "INSERT INTO CRIMETYPE VALUES(%s, %s, %s)",
"DropCrimeType": "DROP TABLE CRIMETYPE",
"DeleteCrimeType": "DELETE FROM CRIMETYPE WHERE TYPEID = %s"
                  }

def GetData():
    typeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/CrimeType/offense_codes.csv")
    with open(actualPath) as csv_file:
        iRow = 1
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            #TODO: The reason why I break in line 7 because there is a file erro in line 8. Fix it later.
            if iRow > 7:
                break
            typeDataList.append((int(row['CODE']), row['NAME'], 'N'))
            iRow += 1
    return typeDataList


def GetSQL(sSqlName):
    return CRIME_TYPE_SQL[sSqlName]

