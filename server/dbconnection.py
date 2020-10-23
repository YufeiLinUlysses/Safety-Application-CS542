import pymysql
from Database import envir # import CreateTable,InsertData,SelectAll
from Database import loc

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

db = DB("CRIMINALANALYSIS").db
# envir.CreateTable(db)
print(envir.SelectAll(db))
print(len(envir.SelectAll(db)))