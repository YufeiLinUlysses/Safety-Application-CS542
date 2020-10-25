import pymysql
import json
import decimal

class DB():
    db = None

    def __init__(self, database):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="123456",
            db=database,
            port=3306
        )

    def dropDB(self, sql):
        dbcur = self.db.cursor()
        try:
            dbcur.execute(sql)
        except Exception as e:
            print(e)
            return None

    def updataDB(self, uUpdate, uData=None):
        pass

    def createDB(self, uCreate):
        dbcur = self.db.cursor()
        sql = uCreate
        try:
            dbcur.execute(sql)
            sqlQuery = "show tables"
            dbcur.execute(sqlQuery)
            rows = dbcur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            self.db.rollback()
            print("Exeception occured:{}".format(e))
    
    def createV(self, uCreate):
        dbcur = self.db.cursor()
        sql = uCreate
        try:
            dbcur.execute(sql)
            sqlQuery = "show full tables"
            dbcur.execute(sqlQuery)
            rows = dbcur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            self.db.rollback()
            print("Exeception occured:{}".format(e))

    def insertDB(self, uInsert, uData):
        insertData = uData
        sql = uInsert
        try:
            dbcur = self.db.cursor()
            dbcur.executemany(sql, insertData)
            self.db.commit()
        except Exception as e:
            print(e)

    def selectDB(self, uSelect, uData=None):
        sql = uSelect
        try:
            dbcur = self.db.cursor()
            if uData == None:
                dbcur.execute(sql)
            else:
                dbcur.execute(sql,uData)
            rows = dbcur.fetchall()
            columns = [desc[0] for desc in dbcur.description]
            result = []
            for row in rows:
                row = [str(val) for val in row]
                row = dict(zip(columns, row))
                result.append(row)
            final = json.dumps(result)
            return final
        except Exception as e:
            self.db.rollback()
            print(e)
            return None
