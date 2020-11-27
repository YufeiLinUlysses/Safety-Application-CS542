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

    def updataDB(self, sSql, data=None):
        self.db.ping(reconnect=True)
        try:

            dbcur = self.db.cursor()
            if data == None:
                dbcur.execute(sSql)
            else:
                dbcur.execute(sSql, data)
            self.db.commit()
        except Exception as e:
            print(e)

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
        self.db.ping(reconnect=True)
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

    def insertDB(self, uInsert, uData=None):
        insertData = uData
        sql = uInsert
        self.db.ping(reconnect=True)
        try:
            dbcur = self.db.cursor()
            if uData == None:
                dbcur.execute(sql)
            else:
                dbcur.executemany(sql, insertData)
            self.db.commit()
        except Exception as e:
            print(e)

    def DeletetDB(self, sSql, uData=None):
        self.db.ping(reconnect=True)
        try:
            dbcur = self.db.cursor()
            if uData == None:
                dbcur.execute(sSql)
            else:
                dbcur.executemany(sSql, uData)
            self.db.commit()
        except Exception as e:
            print(e)

    def insertByOneDB(self, uInsert, uData):
        sql = uInsert
        for i in uData:
            try:
                dbcur = self.db.cursor()
                dbcur.execute(sql, i)
            except Exception as e:
                print(e)
                continue
        self.db.commit()

    def InsertWithErrorMessage(self, sSql, data=None):
        self.db.ping(reconnect=True)
        try:
            dbcur = self.db.cursor()
            if data == None:
                dbcur.execute(sSql)
            else:
                dbcur.executemany(sSql, data)
            self.db.commit()

        except Exception as e:
            return False
        return True

    def selectDB(self, uSelect, uData=None):
        sql = uSelect
        dbcur = self.db.cursor()
        try:

            if uData == None:
                dbcur.execute(sql)
            else:
                dbcur.execute(sql, uData)
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
            return {"Exception": e}

    def CreateTrigger(self, sSql):
        self.db.ping(reconnect=True)
        try:
            dbcur = self.db.cursor()
            dbcur.execute(sSql)
            self.db.commit()
        except Exception as e:
            print(e)

    def DropTrigger(self, sSql):
        self.db.ping(reconnect=True)
        try:
            dbcur = self.db.cursor()
            dbcur.execute(sSql)
            self.db.commit()
        except Exception as e:
            print(e)

    def AddFunction(self, sSql):
        self.db.ping(reconnect=True)
        try:
            dbcur = self.db.cursor()
            dbcur.execute(sSql)
            self.db.commit()
        except Exception as e:
            print(e)


