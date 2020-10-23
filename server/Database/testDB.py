# Author: Yufei Lin
# Email: ylin9@wpi.edu
# Only use it to create in test database
import json

def createTestTable(dbcon):
    dbcur = dbcon.cursor()
    sql = '''CREATE TABLE gdp(
                   country varchar(32), 
                   value float(10,2)
                )'''
    
    try:
        dbcur.execute(sql)
        sqlQuery = "show tables"
        dbcur.execute(sqlQuery)
        rows = dbcur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Exeception occured:{}".format(e))

def fetchAllFromGDP(dbcon):
    sql = "Select * from gdp"
    try: 
        dbcur = dbcon.cursor()
        dbcur.execute(sql)
        rows = dbcur.fetchall()
        columns = [desc[0] for desc in dbcur.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        final = json.dumps(result)
        return final
    except Exception as e:
        print(e)
        return None

def insertGDPData(dbcon):
    gdpData = [
        ("USA", 20.5),
        ("China", 13.4),
        ("Germany", 4.0),
        ("Japan", 4.9),
        ("France", 2.8),
    ]
    sql = 'INSERT INTO gdp VALUES(%s, %s)'
    try: 
        dbcur = dbcon.cursor()
        dbcur.executemany(sql, gdpData)
        dbcon.commit()
    except Exception as e:
        print(e)

