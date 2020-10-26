from LOCATION import *
import pymysql

#print(GetLocation())
#print(GetLocation())

GetLocation()

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db="test",
    port=3306
)


CreateLocation(db)
InsertLocation(db)
print('u')
SelectAllLocation(db)