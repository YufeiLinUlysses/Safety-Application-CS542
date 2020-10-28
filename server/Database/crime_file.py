# Author: Torres Fan
# Email: xfan3@wpi.edu

import json
import csv
# import checkTables
import os



CRIME_SQL = {"CreateCrime": """CREATE TABLE CRIMEFILE 
            (CRIMEID INT PRIMARY KEY, 
            LOCATIONID INT,
            TYPEID INT,
            TIMESTAMP INT,
            FOREIGN KEY (LOCATIONID) REFERENCES LOCATION(LOCATIONID),
            FOREIGN KEY (TYPEID) REFERENCES CRIMETYPE(TYPEID),
            FOREIGN KEY (TIMESTAMP) REFERENCES ENVIRONMENT(WDATE))
            """,
            "SelectByID": "Select * from CRIMEFILE where CRIMEID = %s",
            "InsertALL": "INSERT INTO CRIMEFILE VALUES(%s, %s, %s, %s)" ,
            "InsertALLIgnore": "INSERT Ignore INTO CRIMEFILE VALUES(%s, %s, %s, %s)" ,
             "DropTable": "DROP TABLE IF EXISTS CRIMEFILE",
             "ColumnNumber": "SELECT COUNT(*) FROM CRIMEFILE"

            }


def GetData():
    crimeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/CrimeFile/finalcrime.csv")
    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            crimeDataList.append((int(row["CRIME_NUMBER"]), 1, int(row["CRIME_TYPE"]), int(row["CRIME_TIME"]))) #as in crime id, loc id, typeID, timeStamp

    return crimeDataList


def GetSql(sql):
    return CRIME_SQL[sql]
