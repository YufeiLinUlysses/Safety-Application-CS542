# Author: Torres Fan
# Email: xfan3@wpi.edu

import crime_file
import crime_type
import loc
import dbconnection



def InitDataBase():
    oDatabase = dbconnection.DB("CRIMINALANALYSIS")
    #oDatabase.createDB(crime_type.GetSQL("CreateCrimeType"))
    oDatabase.insertDB(crime_type.GetSQL("InsertALL2CrimeType"), crime_type.GetData())
InitDataBase()

