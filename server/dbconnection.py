import pymysql
from Database.envir import CreateTable,InsertData,SelectAll

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
print(SelectAll(db))