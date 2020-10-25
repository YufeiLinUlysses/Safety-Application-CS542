import json
import csv

CREATE_SQL = {"CreateInvolve": "CREATE TABLE INVOLVE (pID INT, crimeID INT, IsVictim Char(1))"}

SELECT_SQL = {"SelectAll": "Select * from INVOLVE",
            "SelectByPIDcrimeID": "Select * from INVOLVE where pID = %s and crimeID = %s"
              }
INSERT_SQL = {"InsertALL": "INSERT INTO INVOLVEFILE VALUES(%s, %s, %s)" }
DROP_SQL = {"DropTable": "DROP TABLE INVOLVEFILE"}

INVOLVE_SQL = {"CreateInvolve": """CREATE TABLE INVOLVE 
                (pID INT, 
                crimeID INT, 
                IsVictim Char(1),
                FOREIGN KEY (pID) REFERENCES PERSONFILE(pid),
                FOREIGN KEY (crimeID) REFERENCES CRIMEFILE(CRIMEID),
                PRIMARY KEY (pID, crimeID))
                """,
               "SelectAll": "Select * from INVOLVE",
               "SelectByPIDcrimeID": "Select * from INVOLVE where pID = %s and crimeID = %s",
               "InsertALL": "INSERT INTO INVOLVE VALUES(%s, %s, %s)" ,
               "DropTable": "DROP TABLE IF EXISTS INVOLVE",
               }


def GetData():
    involveDataList = []
    for i in range(1, 8):
        involveDataList.append((169293571, i, 'Y'))

    return involveDataList

def GetSQL(sql):
    return INVOLVE_SQL[sql]