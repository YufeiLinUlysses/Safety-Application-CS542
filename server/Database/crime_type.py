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
    crimeTypeList = []
    with open('crime.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
            elif line_count > 3:
                break
            else:
                crimeDataList.append((line_count, int(row[1]), row[2], row[3], row[6]))
            line_count += 1

    return crimeTypeList