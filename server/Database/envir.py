# Author: Yufei Lin
# Email: ylin9@wpi.edu
import json
import csv

ENV_SQL = {"CreateEnv": """CREATE TABLE ENVIRONMENT(
                                WDATE INT,
                                HOUR INT,
                                TEMP INT,
                                HUMIDITY INT,
                                WINDSPEED INT,
                                PRESSURE INT,
                                VISIBILITY INT,
                                SUNRISE INT,
                                SUNSET INT,
                                WEATHER VARCHAR(128),
                                PRECIPITATION FLOAT,
                                PRIMARY KEY(WDATE, HOUR))""",
           "InsertALL": '''INSERT INTO ENVIRONMENT VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
           "DropTable": "DROP TABLE IF EXISTS ENVIRONMENT",
           # Select Related SQL
           "SelectAll": "Select * from ENVIRONMENT",
           "CntWeather": '''(SELECT WEATHER AS text, COUNT(*) AS value 
                                FROM ENVIRONMENT 
                                GROUP BY WEATHER) 
                                ORDER BY value DESC''',
           # View Summary by Date
           "createViewSum": '''CREATE VIEW SUMMARY AS
                                SELECT 
                                    WDATE,
                                    MIN(WINDSPEED) AS minW, 
                                    AVG(WINDSPEED) AS avgW,
                                    MAX(WINDSPEED) AS maxW,
                                    MIN(TEMP) AS minT, 
                                    AVG(TEMP) AS avgT,
                                    MAX(TEMP) AS maxT,
                                    MIN(HUMIDITY) AS minH, 
                                    AVG(HUMIDITY) AS avgH,
                                    MAX(HUMIDITY) AS maxH,
                                    MIN(PRECIPITATION) AS minP, 
                                    AVG(PRECIPITATION) AS avgP,
                                    MAX(PRECIPITATION) AS maxP
                                FROM
                                    ENVIRONMENT
                                GROUP by WDATE''',
           "dropViewSum": "DROP VIEW SUMMARY",
           "selectAllSum": "SELECT * FROM SUMMARY",
           # wind speed by month
           "wsM": '''SELECT 
                            MONTH(FROM_UNIXTIME(WDATE)) AS m, 
                            AVG(avgW) AS avgW,
                            MAX(avgW) AS maxW,
                            MIN(avgW) AS minW
                          FROM SUMMARY 
                          GROUP BY MONTH(FROM_UNIXTIME(WDATE))''',
           # temperature by month
           "tM": '''SELECT 
                            MONTH(FROM_UNIXTIME(WDATE)) AS m, 
                            AVG(avgT) AS avgT,
                            MAX(avgT) AS maxT,
                            MIN(avgT) AS minT
                          FROM SUMMARY 
                          GROUP BY MONTH(FROM_UNIXTIME(WDATE))''',
           # humidity by month
           "hM": '''SELECT 
                            MONTH(FROM_UNIXTIME(WDATE)) AS m, 
                            AVG(avgH) AS avgH,
                            MAX(avgH) AS maxH,
                            MIN(avgH) AS minH
                          FROM SUMMARY 
                          GROUP BY MONTH(FROM_UNIXTIME(WDATE))''',
           # pressure by month
           "pM": '''SELECT 
                            MONTH(FROM_UNIXTIME(WDATE)) AS m, 
                            AVG(avgP) AS avgP,
                            MAX(avgP) AS maxP,
                            MIN(avgP) AS minP
                          FROM SUMMARY 
                          GROUP BY MONTH(FROM_UNIXTIME(WDATE))''',
           # weather - crime
           "wC": '''(SELECT  W As weather, COUNT(T) AS value FROM 
                      (SELECT DISTINCT CRIMEFILE.TYPEID AS T, 
                                       ENVIRONMENT.WEATHER AS W 
                      FROM CRIMEFILE
                      JOIN ENVIRONMENT 
                      ON CRIMEFILE.TIMESTAMP=ENVIRONMENT.WDATE) TEMP
                      GROUP BY W )
                      ORDER BY value DESC LIMIT 15;''',
           # humidity - crime
           "hC": '''SELECT * FROM (
                        SELECT DISTINCT TYPEID AS T, AVGH 
                        FROM CRIMEFILE 
                        JOIN Summary 
                        ON CRIMEFILE.TIMESTAMP=Summary.WDATE) TEMP ''',
           # temperature - crime
           "tC": '''SELECT * FROM (
                        SELECT DISTINCT TYPEID AS T, AVGT 
                        FROM CRIMEFILE 
                        JOIN Summary 
                        ON CRIMEFILE.TIMESTAMP=Summary.WDATE) TEMP ''',
           # windspeed - crime
           "wsC": '''SELECT * FROM (
                        SELECT DISTINCT TYPEID AS T, AVGW 
                        FROM CRIMEFILE 
                        JOIN Summary 
                        ON CRIMEFILE.TIMESTAMP=Summary.WDATE) TEMP ''',
           # pressure - crime
           "pC": '''SELECT * FROM (
                        SELECT DISTINCT TYPEID AS T, AVGP 
                        FROM CRIMEFILE 
                        JOIN Summary 
                        ON CRIMEFILE.TIMESTAMP=Summary.WDATE) TEMP ''',
           }


def GetData():
    with open('./DataSource/Environment/bosFinal.csv') as f:
        f.readline()
        envData = [tuple(line) for line in csv.reader(f)]
    return envData


def GetSQL(sql):
    return ENV_SQL[sql]
