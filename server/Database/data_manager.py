# Author: Torres Fan
# Email: xfan3@wpi.edu

import crime_file
import crime_type
import loc
import dbconnection
import person_file
import involve


def InitDataBase():
    oDatabase = dbconnection.DB("CRIMINALANALYSIS")
    #oDatabase.createDB(crime_type.GetSQL("CreateCrimeType"))
    #oDatabase.insertDB(crime_type.GetSQL("InsertALL2CrimeType"), crime_type.GetData())
    # oDatabase.createDB(loc.GetSQL("CREATELOCATION"))
    # oDatabase.insertDB(loc.GetSQL("INSERTALL"), loc.GetData())
    # oDatabase.dropDB(person_file.GetSQL("DropTable"))
    # oDatabase.createDB(person_file.GetSQL("CreatePerson"))
    # oDatabase.insertDB(person_file.GetSQL("InsertALL"), person_file.GetData())
    # oDatabase.dropDB(crime_file.GetSql("DropTable"))
    # oDatabase.createDB(crime_file.GetSql("CreateCrime"))
    # oDatabase.insertDB(crime_file.GetSql("InsertALL"), crime_file.GetData())
    oDatabase.dropDB(involve.GetSQL("DropTable"))
    oDatabase.createDB(involve.GetSQL("CreateInvolve"))
    oDatabase.insertDB(involve.GetSQL("InsertALL"), involve.GetData())

InitDataBase()

