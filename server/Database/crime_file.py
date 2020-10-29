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
            TIMESLOT INT,
            FOREIGN KEY (LOCATIONID) REFERENCES LOCATION(LOCATIONID),
            FOREIGN KEY (TYPEID) REFERENCES CRIMETYPE(TYPEID),
            FOREIGN KEY (TIMESTAMP, TIMESLOT) REFERENCES ENVIRONMENT(WDATE, HOUR))
            """,
            "SelectByID": "Select * from CRIMEFILE where CRIMEID = %s",
            "InsertALL": "INSERT INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s)" ,
            "InsertALLIgnore": "INSERT Ignore INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s)" ,
             "DropTable": "DROP TABLE IF EXISTS CRIMEFILE",
             "ColumnNumber": "SELECT COUNT(*) FROM CRIMEFILE",

             "TimeSlotTrigger": """
             
                CREATE TRIGGER TimeSlotInsert
                BEFORE INSERT
                ON CRIMEFILE FOR EACH ROW
                Begin
                If (New.TIMESLOT not in (0, 3, 6, 9, 12, 15, 18, 21)) Then
                   SET NEW.TIMESLOT = ((new.TIMESLOT div 3) * 3);
                end if;
                END
             """,
             "DropSlotTrigger": "drop trigger if exists TimeSlotInsert",

            }


def GetData():
    crimeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/CrimeFile/finalcrime.csv")
    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            crimeDataList.append((int(row["CRIME_NUMBER"]), int(row["LOC_ID"]), int(row["CRIME_TYPE"]), int(row["CRIME_TIME"]), int(row["HOUR"]))) #as in crime id, loc id, typeID, timeStamp

    return crimeDataList


def GetSql(sql):
    return CRIME_SQL[sql]
