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
"DropTable": "DROP TABLE IF EXISTS CRIMETYPE",
"DeleteCrimeType": "DELETE FROM CRIMETYPE WHERE TYPEID = %s",
'typecnt': 'SELECT DESCRIPTION,COUNT(CRIMEID) ct FROM CRIMEFILE JOIN CRIMETYPE ON CRIMEFILE.TYPEID = CRIMETYPE.TYPEID GROUP BY DESCRIPTION ORDER BY COUNT(CRIMEID) DESC' 
                  }

def GetData():
    typeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/CrimeType/offense_codes.csv")
    with open(actualPath, encoding="gbk") as csv_file:
        iRow = 1
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        idList = []
        for row in csv_reader:
            #TODO: Change in trigger
            if int(row['CODE']) in idList:
                continue
            idList.append(int(row['CODE']))
            typeDataList.append((int(row['CODE']), row['NAME'], 'N'))
            iRow += 1
    return typeDataList


def GetSQL(sSqlName):
    return CRIME_TYPE_SQL[sSqlName]

