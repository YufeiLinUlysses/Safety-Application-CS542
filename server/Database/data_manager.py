# Author: Torres Fan
# Email: xfan3@wpi.edu

import crime_file
import crime_type
import loc
import dbconnection
import person_file
import involve
import envir
import insert_table
import relation_table

oDatabase = dbconnection.DB("CRIMINALANALYSIS")

def test():
    print(GetCrimeFileByLoc(42.2762, -71.0955))

def GetCrimeFileByLoc(sLat, sLon):
    sSql = crime_file.GetSql("SelectCrimeByLoc")
    return oDatabase.selectDB(sSql, (sLat, sLat, sLon, sLon))

def GetCrimeCases():
    print(oDatabase.selectDB(crime_file.GetSql("ColumnNumber")))

def GetPeopleNumber():
    print(oDatabase.selectDB(person_file.GetSQL("ColumnNumber")))

def CreateCrimeTimeTrigger():
    oDatabase.CreateTrigger(crime_file.GetSql("TimeSlotTrigger"))

#TODO: return 1 if success?
def Insert2Insert(insertData):
    sName = insertData.get("name")
    sNameState = insertData.get("nameState")
    sCriminal = insertData.get("criminal")
    sVictim = insertData.get("victim")
    sRelation = insertData.get("relation")
    sType = insertData.get("type")
    sName = insertData.get("name")
    sLat = insertData.get("latitude")
    sLon = insertData.get("longitude")
    sTime = insertData.get("ctime")
    sDate = insertData.get("cdate")
    insertData = ((sName, sNameState, sCriminal, sVictim, sRelation,sType, sName, sLat, sLon, sTime, sDate))
    oDatabase.insertDB(insert_table.GetSql("INSERT_SQL"), insertData)



def InitDataBase():
    pass
    #sequence is important here because we have foreign key constraint.
    # try:
    #     oDatabase.dropDB(involve.GetSQL("DropTable"))
    # except:
    #     print("involve not dropped")
    # try:
    #     oDatabase.dropDB(crime_file.GetSql("DropTable"))
    # except:
    #     print("crime_file not dropped")
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
    #oDatabase.insertDB(crime_type.GetSQL("InsertAllIgnore"), crime_type.GetData())
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
    # Init for Person
    #oDatabase.createDB(person_file.GetSQL("CreatePerson"))
    #oDatabase.insertDB(person_file.GetSQL("InsertALL"), person_file.GetData())
    # #
    # Init for Crime File
    # oDatabase.createDB(crime_file.GetSql("CreateCrime"))
    # #oDatabase.insertDB(crime_file.GetSql("InsertALL"), crime_file.GetData())
    # CreateCrimeTimeTrigger()
    # oDatabase.insertDB(crime_file.GetSql("InsertALLIgnore"), crime_file.GetData())
    #
    # #
    # Init for Involve
    #oDatabase.createDB(involve.GetSQL("CreateInvolve"))
    oDatabase.insertDB(involve.GetSQL("InsertALL"), involve.GetData())
    #
    #
    # # init for relation
    # oDatabase.createDB(relation_table.GetSQL("CREATE_RELATION"))


    #
    # #init for insert_table
    # oDatabase.createDB(insert_table.GetSql("CreateInsertion"))






InitDataBase()
#test()
# GetCrimeCases()
# GetPeopleNumber()


