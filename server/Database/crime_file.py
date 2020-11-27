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
			POLICE_DISTRICT VARCHAR(25),
			ERRORINDICATE VARCHAR(25) NOT NULL,
            FOREIGN KEY (POLICE_DISTRICT) REFERENCES LOCATION(POLICE_DISTRICT),
            FOREIGN KEY (TYPEID) REFERENCES CRIMETYPE(TYPEID),
            FOREIGN KEY (TIMESTAMP, TIMESLOT) REFERENCES ENVIRONMENT(WDATE, HOUR))
            """,
             "SelectByID": "Select * from CRIMEFILE where CRIMEID = %s",
             "InsertALL": "INSERT INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
             "InsertALLIgnore": "INSERT Ignore INTO CRIMEFILE VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
             "DropTable": "DROP TABLE IF EXISTS CRIMEFILE",
             "ColumnNumber": "SELECT COUNT(*) FROM CRIMEFILE",

             "InsertTrigger": """
                CREATE TRIGGER CRIMEINSERT
                BEFORE INSERT ON CRIMEFILE 
                FOR EACH ROW
                Begin
                If (New.TIMESLOT not in (0, 3, 6, 9, 12, 15, 18, 21)) Then
                   SET NEW.TIMESLOT = ((new.TIMESLOT div 3) * 3);
                end if;
                If New.LAT = -1 OR NEW.LAT = 0 Then
                  SIGNAL SQLSTATE '45000';
                end if;
                END
             """,

             "DropInsertTrigger": "drop trigger if exists insertTrigger",

             "DistanceFunc": """
             CREATE FUNCTION CORDISTANCE(    
                LATORI FLOAT,
                LNGORI FLOAT,
                LATDEST FLOAT,
                LNGDEST FLOAT
                )  
                RETURNS FLOAT 
                DETERMINISTIC 
                BEGIN  
                DECLARE R FLOAT;
                DECLARE DLAT FLOAT;
                DECLARE DLON FLOAT;
                DECLARE A FLOAT;
                DECLARE DIST FLOAT;
                SET R = 6371;
                SET DLAT = RADIANS(LATORI-LATDEST);
                SET DLON = RADIANS(LNGORI-LNGDEST);
                SET A = POWER(SIN(DLAT/2),2)+COS(RADIANS(LATDEST))*COS(RADIANS(LATORI))*POWER(SIN(DLON/2),2);
                SET DIST = 2*R*ATAN2(SQRT(a),SQRT(1-a)); 
                RETURN DIST; 
                END
             """,

             "SelectCrimeTypeByLoc": """T.DESCRIPTION,C.LAT, C.LON
             from CRIMEFILE C, CRIMETYPE T 
             where  C.TYPEID = T.TYPEID and 
             abs(C.LAT- %s) <= 1e-6 and abs(C.LON- %s) <= 1e-6
             Order by abs(C.LAT- %s) + abs(C.LON- %s)
             Limit 5
             """,
             'SelectCrimeByLoc': '''SELECT DISTINCT LAT, LON
              FROM CRIMEFILE 
              WHERE CORDISTANCE(LAT, LON, %s, %s) <=3 
              ORDER BY CORDISTANCE(LAT, LON, %s, %s) 
              LIMIT 10;''',

             "SelectMAXID": "Select max(CRIMEID) From crimefile",


             "InsertFromInsertion": """
             INSERT INTO CRIMEFILE (LAT, LON, TIMESTAMP, TIMESLOT, TYPEID, POLICE_DISTRICT, CRIMEID)
                        Select I.LAT, I.LON, I.TIMESTAMP, I.TIMESLOT, C.TYPEID, I.POLICE_DISTRICT, %s as CRIMEID
                        From Insertion I, CrimeType C 
                        where I.CONFIRMED = True and I.CrimeType = C.DESCRIPTION""",

             "InsertCrimePeople": """
             INSERT INTO PERSONFILE (pid)
                Select CriminalID
                From Insertion 
                where CONFIRMED = True
             """,
             "InsertVictimPeople": """
             INSERT INTO PERSONFILE (pid)
                        Select VictimID
                        From Insertion
                        where CONFIRMED = True
             """,
             "InsertInvolve": """
             INSERT INTO INVOLVE (pid, isVictim, crimeID)
                        Select VictimID, 'Y' as isVictim, %s as crimeID
                        From Insertion
                        where CONFIRMED= True
             """,
             "InsertInvolveCrime": """
             INSERT INTO INVOLVE (pid, isVictim, crimeID)
                        Select CriminalID, 'N' as isVictim, %s as crimeID
                        From Insertion
                        where CONFIRMED= True
             """,
             "InsertRelation": """
             INSERT INTO RelationTable (pid1, pid2, relation)
                        Select VictimID, CriminalID, Relation
                        From Insertion
                        where CONFIRMED = True   
             """,

             "TimeslotCount": """SELECT TIMESLOT, COUNT(*) AS NUM FROM (SELECT DESCRIPTION, TIMESLOT, POLICE_DISTRICT, DIST FROM 
                                       (SELECT * FROM 
			                                 (SELECT TYPEID,
					                                 TIMESLOT,
					                                 POLICE_DISTRICT,
					                                 CORDISTANCE(LAT, LON, %s,%s) AS DIST
                                              FROM CRIMEFILE
			                                  ORDER BY DIST) TEMP
                                        WHERE DIST < 1) FINAL
                                        JOIN 
                                        CRIMETYPE
                                        ON FINAL.TYPEID=CRIMETYPE.TYPEID) RESULT
                                        GROUP BY TIMESLOT 
                                        ORDER BY NUM DESC""",
             "PoliceDCount": """SELECT POLICE_DISTRICT, COUNT(*) AS NUM FROM (SELECT DESCRIPTION, TIMESLOT, POLICE_DISTRICT, DIST FROM 
                                       (SELECT * FROM 
			                                 (SELECT TYPEID,
					                                 TIMESLOT,
					                                 POLICE_DISTRICT,
					                                 CORDISTANCE(LAT, LON, %s,%s) AS DIST
                                              FROM CRIMEFILE
			                                  ORDER BY DIST) TEMP
                                        WHERE DIST < 1) FINAL
                                        JOIN 
                                        CRIMETYPE
                                        ON FINAL.TYPEID=CRIMETYPE.TYPEID) RESULT
                                        GROUP BY POLICE_DISTRICT 
                                        ORDER BY NUM DESC""",
             "CTypeCount": """SELECT DESCRIPTION, COUNT(*) AS NUM FROM (SELECT DESCRIPTION, TIMESLOT, POLICE_DISTRICT, DIST FROM 
                                       (SELECT * FROM 
			                                 (SELECT TYPEID,
					                                 TIMESLOT,
					                                 POLICE_DISTRICT,
					                                 CORDISTANCE(LAT, LON, %s,%s) AS DIST
                                              FROM CRIMEFILE
			                                  ORDER BY DIST) TEMP
                                        WHERE DIST < 1) FINAL
                                        JOIN 
                                        CRIMETYPE
                                        ON FINAL.TYPEID=CRIMETYPE.TYPEID) RESULT
                                        GROUP BY DESCRIPTION 
                                        ORDER BY NUM DESC""",
             "DistrictCount": """SELECT DISTRICT, COUNT(*) 
                                 FROM CRIMEFILE JOIN LOCATION 
                                 ON CRIMEFILE.POLICE_DISTRICT = LOCATION.POLICE_DISTRICT 
                                 GROUP BY DISTRICT""",
             "UpdateSafety": """Update location L join 
                                (SELECT count(*) as C, police_district
                                from crimefile
                                group by POLICE_DISTRICT) as Temp 
                                on L.police_district = Temp.police_district
                                Set L.safetyIndex = Temp.C""",
             }


def GetData():
    crimeDataList = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(
        script_dir, "DataSource/CrimeFile/finalcrime.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            crimeDataList.append((int(row["CRIME_NUMBER"]), int(row["CRIME_TYPE"]), int(row["CRIME_TIME"]),
                                  int(row["HOUR"]), row["LAT"], row["LONG"], row["STREET"], row["POLICEDISTRICT"], '1'))
    return crimeDataList


def GetSql(sql):
    return CRIME_SQL[sql]
