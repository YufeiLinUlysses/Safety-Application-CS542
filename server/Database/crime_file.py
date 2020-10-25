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
            FOREIGN KEY (TYPEID) REFERENCES CRIMETYPE(TYPEID))
            """,
            "SelectByID": "Select * from CRIMEFILE where CRIMEID = %s",
            "InsertALL": "INSERT INTO CRIMEFILE VALUES(%s, %s, %s, %s)" ,
             "DropTable": "DROP TABLE IF EXISTS CRIMEFILE"
            }


def GetData():
    crimeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/CrimeFile/crime.csv")
    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 1

        for row in csv_reader:
            if line_count > 7:
                break
            #becauseof offense code foreign key constraints, we currently fix offense code
            #crimeDataList.append((line_count, line_count, int(row["OFFENSE_CODE"]), 1)) #as in crime id, loc id, typeID, timeStamp
            crimeDataList.append((line_count, line_count, 612, 1))
            line_count += 1

    return crimeDataList


def GetSql(sql):
    return CRIME_SQL[sql]

