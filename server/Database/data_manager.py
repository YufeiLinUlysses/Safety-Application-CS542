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


def InitDataBase():
    pass
    # sequence is important here because we have foreign key constraint.
    # try:
    # oDatabase.dropDB(relation_table.GetSQL("DROP"))
    # except:
    # print("relation not dropped")
    # try:
    # oDatabase.dropDB(involve.GetSQL("DropTable"))
    # except:
    # print("involve not dropped")
    # try:
    # oDatabase.dropDB(crime_file.GetSql("DropTable"))
    # except:
    # print("crime_file not dropped")
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
    # oDatabase.insertDB(loc.GetSQL("INSERTALL"), loc.GetData())
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
    # oDatabase.createDB(crime_file.GetSql("CreateCrime"))
    # CreateCrimeFileTrigger()
    # oDatabase.insertByOneDB(crime_file.GetSql(
    # "InsertALLIgnore"), crime_file.GetData())
    #
    # #
    #Init for Involve
    # oDatabase.createDB(involve.GetSQL("CreateInvolve"))
    # oDatabase.insertDB(involve.GetSQL("InsertALL"), involve.GetData())


    # init for relation
    #oDatabase.createDB(relation_table.GetSQL("CREATE_RELATION"))

    #
    #init for insert_table
    oDatabase.createDB(insert_table.GetSql("CreateInsertion"))


def createEnvSummary():
    oDatabase.createV(envir.GetSQL("createViewSum"))



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


def AddDisFunc():
    oDatabase.AddFunction(crime_file.GetSql("DistanceFunc"))

def UpdateSafetyIndex():
    oDatabase.updataDB(crime_file.GetSql("UpdateSafety"))



#InitDataBase()
# createEnvSummary()
# GetCrimeCases()
# GetPeopleNumber()
# AddDisFunc()
UpdateSafetyIndex()