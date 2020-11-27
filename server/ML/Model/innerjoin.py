# written by Jingfeng Xia, jxia@wpi.edu

import Get_Data
import dbconnection

# all missing parts were done on local mysqldb, will be filled in future
# get data from "offense_codes.csv" and "crime_info.csv"

OCData = Get_Data.Get_OFFENSE_CODE_Data()
CIData = Get_Data.Get_CRIME_INFO_Data()

# All sql quries

Create_OC = "CREATE TABLE OFFENSE_CODE( CODE char(4) primary key, NAME varchar(64) not null, DANGER char(1) not null)"
Create_CI = "CREATE TABLE CRIME_INFO(CRIME_NUMBER char(6) primary key, OFFENSE_CODE char(4), MONTH char(2), \ 
    DAY_OF_WEEK char(10), DISTRICT char(3) not null, HOUR char(2), LATTITUDE char(12) not null, \ 
    LONGTITUDE char(12) not null, SHOOTING char(1), \ 
    FOREIGN KEY (OFFENSE_CODE) REFERENCES OFFENSE_CODE(CODE);"

InsertALL_OC = "INSERT ignore INTO OFFENSE_CODE VALUES(%s, %s, %s)"
InsertALL_CI = "INSERT ignore INTO CRIME_INFO VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Trigger * 3
# Innerjoin

# Create and insert data into 2 tables

toDatabase = dbconnection.DB("safety_index")
toDatabase.createDB(Create_OC)
toDatabase.insertDB(InsertALL_OC, OCData)
toDatabase.createDB(Create_CI)
toDatabase.insertDB(InsertALL_CI, CIData)

# innerjoin
# output innerjoin.csv
