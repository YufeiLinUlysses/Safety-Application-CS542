# Author: Torres Fan
# Email: xfan3@wpi.edu
from . import crime_file
from . import crime_type
from . import loc
from . import dbconnection
from . import person_file
from . import involve
from . import envir
from . import insert_table
from . import relation_table

oDatabase = dbconnection.DB("CRIMINALANALYSIS")


def InitDataBase():
    pass
    # sequence is important here because we have foreign key constraint.
    # try:
    #     oDatabase.dropDB(relation_table.GetSQL("DROP"))
    # except:
    #     print("relation not dropped")
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
    # oDatabase.createDB(crime_type.GetSQL("CreateCrimeType"))
    # oDatabase.insertDB(crime_type.GetSQL("InsertAllIgnore"), crime_type.GetData())

    #
    # # Init for Location
    # oDatabase.createDB(loc.GetSQL("CREATELOCATION"))
    #oDatabase.insertDB(loc.GetSQL("INSERTALL"), loc.GetData())
    #
    # Init for Environment
    # oDatabase.createDB(envir.GetSQL("CreateEnv"))
    # oDatabase.insertDB(envir.GetSQL("InsertALL"), envir.GetData())
    #
    # Init for Person
    # oDatabase.createDB(person_file.GetSQL("CreatePerson"))
    # oDatabase.insertDB(person_file.GetSQL("InsertALL"), person_file.GetData())
    # #
    # Init for Crime File
    oDatabase.createDB(crime_file.GetSql("CreateCrime"))
    CreateCrimeFileTrigger()
    oDatabase.insertDB(crime_file.GetSql(
        "InsertALLIgnore"), crime_file.GetData())
    #
    # #
    # Init for Involve
    # oDatabase.createDB(involve.GetSQL("CreateInvolve"))
    #oDatabase.insertDB(involve.GetSQL("InsertALL"), involve.GetData())
    #
    #
    # # init for relation
    # oDatabase.createDB(relation_table.GetSQL("CREATE_RELATION"))

    #
    # #init for insert_table
    # oDatabase.createDB(insert_table.GetSql("CreateInsertion"))


def test():
    print(GetCrimeFileByLoc(42.35779190, -71.13937378))
    print(GetCrimeFileByLoc(-1, -1))


def GetCrimeFileByLoc(sLat, sLon):
    sSql = crime_file.GetSql("SelectCrimeByLoc")
    return oDatabase.selectDB(sSql, (sLat, sLon, sLat, sLon))


def GetCrimeCases():
    print(oDatabase.selectDB(crime_file.GetSql("ColumnNumber")))


def GetPeopleNumber():
    print(oDatabase.selectDB(person_file.GetSQL("ColumnNumber")))


def CreateCrimeFileTrigger():
    oDatabase.DropTrigger(crime_file.GetSql("DropInsertTrigger"))
    oDatabase.CreateTrigger(crime_file.GetSql("InsertTrigger"))

# TODO: return 1 if success?


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
    insertData = ((sName, sNameState, sCriminal, sVictim,
                   sRelation, sType, sName, sLat, sLon, sTime, sDate))
    oDatabase.insertDB(insert_table.GetSql("INSERT_SQL"), insertData)


# InitDataBase()
# test()
# GetCrimeCases()
# GetPeopleNumber()
