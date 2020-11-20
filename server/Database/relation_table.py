RELATION_SQL = {
"CREATE_RELATION":
            """CREATE TABLE RelationTable 
            (PID1 INT,
            PID2 INT,
            Relation varchar(255),
            PRIMARY KEY(PID1, PID2))
            """,
}





def GetSQL(sqlName):
    return RELATION_SQL[sqlName]