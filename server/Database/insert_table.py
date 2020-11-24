INSERTION_SQL = {"CreateInsertion": """CREATE Table Insertion 
                                        (LAT FLOAT(24, 8) Not NULL, 
                                        LON FLOAT(24, 8) Not NULL,
                                        TIMESTAMP INT Not NULL,
                                        TIMESLOT INT Not NULL,
                                        Relation VARChar(30) NOT NULL,
                                        CriminalID varchar(100),
                                        VictimID varchar(100),
                                        CrimeType varchar(50))""",
                 "INSERT_SQL": "INSERT ignore INTO Insertion VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                 }


def GetSql(sql):
    return INSERTION_SQL[sql]
