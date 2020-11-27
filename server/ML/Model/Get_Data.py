# written by Jingfeng Xia, jxia@wpi.edu

# pysql code deriveded from Xuhui Fan

import os
import csv

def Get_OFFENSE_CODE_Data():
    OFFENSE_CODE_List = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(
        script_dir, "../Data/offense_codes.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            OFFENSE_CODE_List.append((str(row["CODE"]), str(row["NAME"]), str(row["DANGER"])))
    return OFFENSE_CODE_List

def Get_CRIME_INFO_Data():
    CRIME_INFO_List = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(
        script_dir, "../Data/crime_info_1.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            CRIME_INFO_List.append(
                (str(row["CRIME_NUMBER"]), str(row["OFFENSE_CODE"]),
                str(row["MONTH"]), str(row["DAY_OF_WEEK"]), 
                str(row["DISTRICT"]),str(row["HOUR"]),
                str(row["Lat"]),str(row["Long"]),str(row["SHOOTING"])))
    return CRIME_INFO_List

def Get_INNERJOINT_Data():
    INNERJOINT_List = []
    script_dir = os.path.dirname(__file__)
    actualPath = os.path.join(
        script_dir, "../Data/innerjoint.csv")

    with open(actualPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
                INNERJOINT_List.append(
                (int(row["CRIME_NUMBER"]), int(row["OFFENSE_CODE"]), str(row["NAME"]),
                int(row["MONTH"]), int(row["DAY_OF_WEEK"]), int(row["HOUR"]),  
                str(row["LATITUDE"]), str(row["LONGTITUDE"]), int(row["SHOOTING"]), int(row["DANGER"])))
    return INNERJOINT_List