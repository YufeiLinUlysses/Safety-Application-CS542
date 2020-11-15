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
    print(GetCrimeFileByLoc(42.2762, -71.0955))

def GetCrimeFileByLoc(sLat, sLon):
    sSql = crime_file.GetSql("SelectCrimeByLoc")
    return oDatabase.selectDB(sSql, (sLat, sLat, sLon, sLon))

def GetCrimeCases():
    print(oDatabase.selectDB(crime_file.GetSql("ColumnNumber")))

def CreateCrimeTimeTrigger():
    oDatabase.CreateTrigger(crime_file.GetSql("TimeSlotTrigger"))



def InitDataBase():
    pass
    #sequence is important here because we have foreign key constraint.
    # try:
    #     oDatabase.dropDB(involve.GetSQL("DropTable"))
    # except:
    #     print("involve not dropped")
    try:
        oDatabase.dropDB(crime_file.GetSql("DropTable"))
    except:
        print("crime_file not dropped")
    # try:
    #     oDatabase.dropDB(person_file.GetSQL("DropTable"))
    # except:
    #     print("person_file not dropped")
    # try:
    #     oDatabase.dropDB(envir.GetSQL("DropTable"))
    # except:
    #     print("envir not dropped")
    # try:
    #     oDatabase.dropDB(loc.GetSQL("DropTable"))
    # except:
    #     print("loc not dropped")
    # try:
    #     oDatabase.dropDB(crime_type.GetSQL("DropTable"))
    # except:
    #     print("crime_type not dropped")

    # Init for Crime Type
    #oDatabase.createDB(crime_type.GetSQL("CreateCrimeType"))
    #oDatabase.insertDB(crime_type.GetSQL("InsertALL2CrimeType"), crime_type.GetData())
    #
    #
    # # Init for Location
    # oDatabase.createDB(loc.GetSQL("CREATELOCATION"))
    # oDatabase.insertDB(loc.GetSQL("INSERTALL"), loc.GetData())
    #
    # # Init for Environment
    # oDatabase.createDB(envir.GetSQL("CreateEnv"))
    # oDatabase.insertDB(envir.GetSQL("InsertALL"), envir.GetData())
    # #
    # # Init for Person
    # oDatabase.createDB(person_file.GetSQL("CreatePerson"))
    # oDatabase.insertDB(person_file.GetSQL("InsertALL"), person_file.GetData())
    # #
    # Init for Crime File
    oDatabase.createDB(crime_file.GetSql("CreateCrime"))
    #oDatabase.insertDB(crime_file.GetSql("InsertALL"), crime_file.GetData())
    CreateCrimeTimeTrigger()
    oDatabase.insertDB(crime_file.GetSql("InsertALLIgnore"), crime_file.GetData())
    #
    # #
    # # # Init for Involve
    # oDatabase.createDB(involve.GetSQL("CreateInvolve"))
    # oDatabase.insertDB(involve.GetSQL("InsertALL"), involve.GetData())





#InitDataBase()
#test()
# GetCrimeCases()


