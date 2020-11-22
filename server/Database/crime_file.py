# Author: Torres Fan
# Email: xfan3@wpi.edu

import json
import csv
import os



CRIME_SQL = {"CreateCrime": """CREATE TABLE CRIMEFILE 
            (CRIMEID INT PRIMARY KEY, 
            TYPEID INT Not NULL,
            TIMESTAMP INT Not NULL,
            TIMESLOT INT Not NULL,
            LAT FLOAT(24, 8) Not NULL, 
			LON FLOAT(24, 8) Not NULL, 
			street VarChar(255),
			POLICE_DISTRICT VARCHAR(25) Not NULL,
			ERRORINDICATE INT NOT NULL,
            FOREIGN KEY (POLICE_DISTRICT) REFERENCES LOCATION(POLICE_DISTRICT),
            FOREIGN KEY (TYPEID) REFERENCES CRIMETYPE(TYPEID),
            FOREIGN KEY (TIMESTAMP, TIMESLOT) REFERENCES ENVIRONMENT(WDATE, HOUR))
            """,
            "SelectByID": "Select * from CRIMEFILE where CRIMEID = %s",
            "InsertALL": "INSERT INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)" ,
            "InsertALLIgnore": "INSERT Ignore INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)" ,
             "DropTable": "DROP TABLE IF EXISTS CRIMEFILE",
             "ColumnNumber": "SELECT COUNT(*) FROM CRIMEFILE",

             "InsertTrigger": """
                CREATE TRIGGER insertTrigger
                BEFORE INSERT ON CRIMEFILE 
                FOR EACH ROW
                Begin
                If (New.TIMESLOT not in (0, 3, 6, 9, 12, 15, 18, 21)) Then
                   SET NEW.TIMESLOT = ((new.TIMESLOT div 3) * 3);
                end if;
                If (New.LAT = -1 and New.LON = -1) Then
                   SET NEW.ERRORINDICATE = 2;
                end if;
                END
             """,

             "DropInsertTrigger": "drop trigger if exists insertTrigger",

             "SelectCrimeByLoc": """Select C.CRIMEID, T.DESCRIPTION, C.STREET, C.LAT, C.LON
             from CRIMEFILE C, LOCATION L, CRIMETYPE T 
             where  C.TYPEID = T.TYPEID and 
             abs(C.LAT- %s) <= 1e-6 and abs(C.LON- %s) <= 1e-6
             Order by abs(C.LAT- %s) + abs(C.LON- %s)
             Limit 5
             """
            }


def GetData():
    crimeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(script_dir, "DataSource/CrimeFile/finalcrime.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            crimeDataList.append((int(row["CRIME_NUMBER"]), int(row["CRIME_TYPE"]), int(row["CRIME_TIME"]),
                                  int(row["HOUR"]), row["LAT"], row["LONG"], row["STREET"], row["POLICEDISTRICT"], 1))
    return crimeDataList


def GetSql(sql):
    return CRIME_SQL[sql]


