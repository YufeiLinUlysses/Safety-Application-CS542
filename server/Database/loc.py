#author:Xiuhan LI
#email: xli14@WPI.EDU

import json
import csv
import os
#still lacking of triggers

LOC_SQL = {'CREATELOCATION': '''CREATE TABLE LOCATION (
	                                   LOCATIONID INT PRIMARY KEY, 
									   STREET VARCHAR(25), 
									   LAT FLOAT(8), 
									   LON FLOAT(8), 
									   POLICE_DISTRICT VARCHAR(5), 
									   DISTRICT VARCHAR(25));''',
			'SELECTALL': 'SELECT * FROM LOCATION',
			'SELECTID': ' SELECT * FROM LOCATION WHERE LOCATIONID = %s',

			"DropTable":"DROP TABLE IF EXISTS LOCATION",
			'INSERTALL': 'INSERT INTO LOCATION VALUES (%s,%s,%s,%s,%s,%s)',
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
									ORDER BY cnt DESC'''
		   }


#copy from yufei
def GetData():
	script_dir = os.path.dirname(__file__)
	actualPath = os.path.join(script_dir, "DataSource/Location/loc.csv")
	locData = []
	with open(actualPath) as f:
		f.readline()
		locData = ([tuple(line) for line in csv.reader(f)])

	return locData


def GetSQL(sql):
	return LOC_SQL[sql]

