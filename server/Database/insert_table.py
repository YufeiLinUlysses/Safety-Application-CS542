INSERTION_SQL = {"CreateInsertion": """CREATE Table Insertion 
            (LOCATION INT,
            Date date,
            Relation Char(30),
            CriminalName varchar(100),
            VictimName varchar(100),
            CrimeType varchar(50),
            CHECK((Relation) is not None),
            """,
            "INSERT_SQL": "INSERT ignore INTO Insertion VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            }

def GetSql(sql):
    return INSERTION_SQL[sql]