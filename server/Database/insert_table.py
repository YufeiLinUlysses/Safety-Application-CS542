INSERTION_SQL = {"CreateInsertion": """CREATE Table Insertion 
                                        (LAT FLOAT(24, 8) Not NULL, 
                                        LON FLOAT(24, 8) Not NULL,
                                        TIMESTAMP BIGINT(50) Not NULL,
                                        TIMESLOT INT Not NULL,
                                        Relation VARChar(30) NOT NULL,
                                        CriminalID varchar(100),
                                        VictimID varchar(100),
                                        CrimeType varchar(50),
                                        CONFIRMED BOOL DEFAULT FALSE)""",
                 "INSERT_SQL": '''INSERT INTO Insertion (LAT, LON, TIMESTAMP, TIMESLOT, RELATION, 
                                  CRIMINALID, VICTIMID, CRIMETYPE) 
                                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'''
                 }


def GetSql(sql):
    return INSERTION_SQL[sql]
