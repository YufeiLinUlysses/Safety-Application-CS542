import json
import csv
import os

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
               "InsertALL": "INSERT ignore INTO INVOLVE VALUES(%s, %s, %s)" ,
               "DropTable": "DROP TABLE IF EXISTS INVOLVE",
               }


def GetData():
    tempDataList = []
    involveDataList = []
    script_dir = os.path.dirname(__file__)
    crimePath = os.path.join(script_dir, "DataSource/CrimeFile/finalcrime.csv")
    peoplePath = os.path.join(script_dir, "DataSource/Person/people.csv")
    with open(crimePath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            tempDataList.append(int(row["CRIME_NUMBER"]))
    with open(peoplePath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        iCrimeRow = 0
        iVictim = 0
        for row in csv_reader:
            if iCrimeRow >= len(tempDataList):
                break
            crimeID = tempDataList[iCrimeRow]
            if iVictim == 0:
                involveDataList.append((int(row["Pid"]), crimeID, 'Y'))
                iVictim += 1
            else:
                involveDataList.append((int(row["Pid"]), crimeID, 'N'))
                iVictim = 0
                iCrimeRow += 1

    return involveDataList

def GetSQL(sql):
    return INVOLVE_SQL[sql]