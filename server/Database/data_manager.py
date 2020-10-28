# Author: Torres Fan
# Email: xfan3@wpi.edu

import crime_file
import crime_type
import loc
import dbconnection
import person_file
import involve
import envir

oDatabase = dbconnection.DB("CRIMINALANALYSIS")

def test():
    print(oDatabase.createV(envir.GetSQL("createViewSum")))

def GetCrimeCases():
    print(oDatabase.selectDB(crime_file.GetSql("ColumnNumber")))

def InitDataBase():
    pass
    # Init for Crime Type
    # try:
    #     oDatabase.dropDB(crime_type.GetSQL("DropTable"))
    #     oDatabase.createDB(crime_type.GetSQL("CreateCrimeType"))
    #     oDatabase.insertDB(crime_type.GetSQL("InsertALL2CrimeType"), crime_type.GetData())
    # except:
    #     pass
    #
    # Init for Location
    # oDatabase.dropDB(loc.GetSQL("DropTable"))
    # oDatabase.createDB(loc.GetSQL("CREATELOCATION"))
    # oDatabase.insertDB(loc.GetSQL("INSERTALL"), loc.GetData())

    # Init for Environment
    # oDatabase.dropDB(envir.GetSQL("DropTable"))
    # oDatabase.createDB(envir.GetSQL("CreateEnv"))
    # oDatabase.insertDB(envir.GetSQL("InsertALL"), envir.GetData())
    #
    # Init for Person
    # oDatabase.dropDB(person_file.GetSQL("DropTable"))
    # oDatabase.createDB(person_file.GetSQL("CreatePerson"))
    # oDatabase.insertDB(person_file.GetSQL("InsertALL"), person_file.GetData())
    #
    # Init for Crime File
    # try:
    #     oDatabase.dropDB(crime_file.GetSql("DropTable"))
    #     oDatabase.createDB(crime_file.GetSql("CreateCrime"))
    #     #oDatabase.insertDB(crime_file.GetSql("InsertALL"), crime_file.GetData())
    #     oDatabase.insertDB(crime_file.GetSql("InsertALLIgnore"), crime_file.GetData())
    # except:
    #     pass
    #
    # # Init for Involve
    # oDatabase.dropDB(involve.GetSQL("DropTable"))
    # oDatabase.createDB(involve.GetSQL("CreateInvolve"))
    # oDatabase.insertDB(involve.GetSQL("InsertALL"), involve.GetData())





#InitDataBase()
# test()
GetCrimeCases()
