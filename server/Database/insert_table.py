INSERTION_SQL = {"CreateInsertion": """CREATE Table Insertion 
                                        (InsertID INT NOT NULL AUTO_INCREMENT,
                                        LAT FLOAT(24, 8) Not NULL, 
                                        LON FLOAT(24, 8) Not NULL,
                                        TIMESTAMP BIGINT(50) Not NULL,
                                        TIMESLOT INT Not NULL,
                                        Relation VARChar(30) NOT NULL,
                                        CriminalID varchar(100),
                                        VictimID varchar(100),
                                        CrimeType varchar(50),
                                        POLICE_DISTRICT varchar(10),
                                        CONFIRMED BOOL DEFAULT FALSE,
                                        Primary key (insertID))""",
                 "INSERT_SQL": '''INSERT INTO Insertion (LAT, LON, TIMESTAMP, TIMESLOT, RELATION, 
                                  CRIMINALID, VICTIMID, CRIMETYPE, POLICE_DISTRICT) 
                                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)''',

                 "TABLE_COUNT": "Select count(*) From insertion",

                 "SELECT_ALL": "Select * from insertion",


                 "UPDATE_TABLE": " UPDATE Insertion SET CONFIRMED = %s WHERE InsertID = %s;",
                 "DELETE_CONFIRM": "DELETE FROM Insertion where CONFIRMED = True",
                 }


def GetSql(sql):
    return INSERTION_SQL[sql]
