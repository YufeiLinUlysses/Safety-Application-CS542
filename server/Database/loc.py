#author:Xiuhan LI
#email: xli14@WPI.EDU

import json
import csv
import os

LOC_SQL = {'CREATELOCATION': '''CREATE TABLE LOCATION (
	                                   POLICE_DISTRICT VARCHAR(25) PRIMARY KEY, 
	                                   DISTRICT VARCHAR(255) Not Null,
									   safetyIndex INT)''',
			'SELECTALL': 'SELECT * FROM LOCATION',
			'SELECTID': ' SELECT * FROM LOCATION WHERE LOCATIONID = %s',

			"DropTable":"DROP TABLE IF EXISTS LOCATION",
			'INSERTALL': 'INSERT IGNORE INTO LOCATION VALUES (%s,%s,%s)',




			'SelectLocation': '''SELECT LAT, LON FROM LOCATION
									JOIN CRIMEFILE 
									ON CRIMEFILE.LOCATIONID = LOCATION.LOCATIONID''',
			'districtCount': '''SELECT COUNT(CRIMEID) AS cnt, DISTRICT FROM LOCATION
									JOIN CRIMEFILE 
									ON CRIMEFILE.LOCATIONID = LOCATION.LOCATIONID 
									GROUP BY DISTRICT
									ORDER BY cnt DESC''',
			'streetCount': '''SELECT COUNT(CRIMEID) AS cnt, STREET FROM LOCATION
									JOIN CRIMEFILE 
									ON CRIMEFILE.LOCATIONID = LOCATION.LOCATIONID 
									GROUP BY STREET
									ORDER BY cnt DESC''',
           'PoliceDs': "SELECT DISTINCT POLICE_DISTRICT FROM LOCATION",
		   }

def GetData():
	locList = []
	script_dir = os.path.dirname(__file__)
	actualPath = os.path.join(script_dir, "DataSource/Location/location.csv")
	with open(actualPath) as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		for row in csv_reader:
			locList.append((row["POLICE_DISTRICT"], row["DISTRICT"], 0))  # as in crime id, loc id, typeID, timeStamp

	return locList


def GetSQL(sql):
	return LOC_SQL[sql]

