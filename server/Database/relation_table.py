RELATION_SQL = {
"CREATE_RELATION":
            """CREATE TABLE RelationTable 
            (PID1 INT,
            PID2 INT,
            Relation varchar(255),
            PRIMARY KEY(PID1, PID2),
            FOREIGN KEY (PID1) REFERENCES PERSONFILE(pid),
            FOREIGN KEY (PID2) REFERENCES PERSONFILE(pid))
            """,

"DROP": "DROP TABLE IF EXISTS RelationTable"
}





def GetSQL(sqlName):
    return RELATION_SQL[sqlName]