import json
import pandas as pd
from pandas import read_csv

#still lacking of triggers
CREATE_SQL = {'CREATELOCATION': 'CREATE TABLE LOCATION (LOCATIONID INT PRIMARY KEY, STREET VARCHAR(25), LAT FLOAT(8), LON FLOAT(8), POLICE_DISTRICT VARCHAR(5), DISTRICT VARCHAR(25));'}
SELECT_SQL = {'SELECTALL': 'SELECT * FROM LOCATION',
			'SELECTID': ' SELECT * FROM LOCATION WHERE LOCATIONID = %s'}
INSERT_SQL = {'INSERTALL': 'INSERT INTO LOCATION VALUES (%s,%s,%s,%s,%s,%s)'}


def GetLocation():
    locationdata = []
    with open('location.csv',encoding='utf8') as f:
    	reader = read_csv(f)
    	reader['LOCATIONID'].astype('int')
    	reader['LAT'].astype('float')
    	reader['LON'].astype('float')
    	# for row in reader:
    	# 	print(row)
    	# 	locationdata.append(row)
    	location.to_csv('new.csv',index = false)
    return reader.head(18467)


def CreateLocation(dbcon):
	dbcur = dbcon.cursor()
	sql = CREATE_SQL['CREATELOCATION']
	try:
		dbcur.execute(sql)
		sqlQuery = "show tables"
		dbcur.execute(sqlQuery)
		rows = dbcur.fetchall()
		for row in rows:
			print(row)
	#what is this?
	except Exception as e:
		print("Exeception occured:{}".format(e))

def SelectAllLocation(dbcon):
	dbcur = dbcon.cursor()
	sql = SELECT_SQL['SELECTALL']
	try:
		dbcur.execute(sql)
		rows = dbcur.fetchall()
		columns = [desc[0] for desc in dbcur.description]
		result = []
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		final = json.dumps(result)
		return final
	except Exception as e:
		print("Exeception occured:{}".format(e))


def SelectLocationId(dbcon, id):
	dbcur = dbcon.cursor()
	sql = SELECT_SQL['SELECTID']
	try:
		dbcur.execute(sql,id)
		rows = dbcur.fecchall()
		columns = [desc[0] for desc in dbcur.description]
		result = []
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		final = json.dumps()
		return final
	except Exception as e:
		print("Exeception occured:{}".format(e))


def InsertLocation(dbcon):
	dbcur = dbcon.cursor()
	sql = INSERT_SQL['INSERTALL']
	locationdata = GetLocation()
	try:
		dbcur.executemany(sql, locationdata)
		dbcon.commit()
	except Exception as e:
		print('Exception occurred:{}'.format(e))


def TestCase(db, iCrimeID=0):
    CreateLocation(db)
    InsertLocation(db)
    result = SelectAllLocation(db)
    #result = SelectLocationId(db, iCrimeID)
    return result