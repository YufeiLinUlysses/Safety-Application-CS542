import json
import csv
import os
#still lacking of triggers
CREATE_SQL = {'CREATELOCATION': '''CREATE TABLE LOCATION (
	                                   LOCATIONID INT PRIMARY KEY, 
									   STREET VARCHAR(25), 
									   LAT FLOAT(8), 
									   LON FLOAT(8), 
									   POLICE_DISTRICT VARCHAR(5), 
									   DISTRICT VARCHAR(25));'''}
SELECT_SQL = {'SELECTALL': 'SELECT * FROM LOCATION',
			'SELECTID': ' SELECT * FROM LOCATION WHERE LOCATIONID = %s'}
INSERT_SQL = {'INSERTALL': 'INSERT INTO LOCATION VALUES (%s,%s,%s,%s,%s,%s)'}

LOC_SQL = {'CREATELOCATION': '''CREATE TABLE LOCATION (
	                                   LOCATIONID INT PRIMARY KEY, 
									   STREET VARCHAR(25), 
									   LAT FLOAT(8), 
									   LON FLOAT(8), 
									   POLICE_DISTRICT VARCHAR(5), 
									   DISTRICT VARCHAR(25));''',
'SELECTALL': 'SELECT * FROM LOCATION',
			'SELECTID': ' SELECT * FROM LOCATION WHERE LOCATIONID = %s',

"DropTable":"DROP TABLE IF EXISTS Location",
'INSERTALL': 'INSERT INTO LOCATION VALUES (%s,%s,%s,%s,%s,%s)',
		   }



def GetData():
	script_dir = os.path.dirname(__file__)
	actualPath = os.path.join(script_dir, "DataSource/Location/location.csv")
	locData = []
	with open(actualPath) as f:
		f.readline()
		for iRow, line in enumerate(csv.reader(f), 1):
			if iRow > 7:
				break
			locData.append(tuple(line))
	return locData

def GetSQL(sql):
	return LOC_SQL[sql]