def createTestTable(dbcon):
    dbcur = dbcon.cursor()
    sql = '''CREATE TABLE gdp(
                   country varchar(32), 
                   value float(10,2)
                )'''
    
    try:
        dbcur.execute(sql)
        sqlQuery = "show tables"
        dbcur.execute(sqlQuery)
        rows = dbcur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Exeception occured:{}".format(e))