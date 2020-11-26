import json
import csv
import os

CRIME_TYPE_SQL = {"CreateCrimeType": """
CREATE TABLE CRIMETYPE 
(TYPEID INT primary key, 
DESCRIPTION varchar(255), 
SHOOTING char(1) default 'N')""",
                  "SelectAllCrimeType": "Select * from CRIMETYPE",
                  "SelectCrimeTypeByCrimeID": "Select * from CRIMETYPE where TYPEID = %s",
                  "InsertALL2CrimeType": "INSERT INTO CRIMETYPE VALUES(%s, %s, %s)",
                  "InsertAllIgnore": "INSERT Ignore INTO CRIMETYPE VALUES(%s, %s, %s)",
                  "DropTable": "DROP TABLE IF EXISTS CRIMETYPE",
                  "DeleteCrimeType": "DELETE FROM CRIMETYPE WHERE TYPEID = %s",
                  'typecnt': 'SELECT DESCRIPTION,COUNT(CRIMEID) ct FROM CRIMEFILE JOIN CRIMETYPE ON CRIMEFILE.TYPEID = CRIMETYPE.TYPEID GROUP BY DESCRIPTION ORDER BY COUNT(CRIMEID) DESC',
                  "SelectAllTypes": "SELECT TYPEID, DESCRIPTION FROM CRIMETYPE"
                  }


def GetData():
    typeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(
        script_dir, "DataSource/CrimeType/offense_codes.csv")
    with open(actualPath, encoding="gbk") as csv_file:
        iRow = 1
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            typeDataList.append((int(row['CODE']), row['NAME'], 'N'))
            iRow += 1
    return typeDataList


def GetSQL(sSqlName):
    return CRIME_TYPE_SQL[sSqlName]
