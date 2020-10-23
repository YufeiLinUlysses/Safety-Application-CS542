import json
import csv

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


def GetData():
    with open('./Database/DataSource/Location/location.csv') as f:
        f.readline()
        locData = [tuple(line) for line in csv.reader(f)]
    return locData


def CreateTable(dbcon):
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

def SelectAll(dbcon):
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


# def SelectLocationId(dbcon, id):
# 	dbcur = dbcon.cursor()
# 	sql = SELECT_SQL['SELECTID']
# 	try:
# 		dbcur.execute(sql,id)
# 		rows = dbcur.fecchall()
# 		columns = [desc[0] for desc in dbcur.description]
# 		result = []
# 		for row in rows:
# 			row = dict(zip(columns,row))
# 			result.append(row)
# 		final = json.dumps()
# 		return final
# 	except Exception as e:
# 		print("Exeception occured:{}".format(e))


def InsertData(dbcon):
	dbcur = dbcon.cursor()
	sql = INSERT_SQL['INSERTALL']
	locData = GetData()
	try:
		dbcur.executemany(sql, locData)
		dbcon.commit()
	except Exception as e:
		print('Exception occurred:{}'.format(e))


# def TestCase(db, iCrimeID=0):
#     CreateLocation(db)
#     InsertLocation(db)
#     result = SelectAllLocation(db)
#     #result = SelectLocationId(db, iCrimeID)
#     return result
GetData()