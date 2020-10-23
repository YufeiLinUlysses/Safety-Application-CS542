def createDatabase(dbcon):
    sql = "CREATE DATABASE IF NOT EXISTS CIMINALANALYSIS"
    try: 
        dbcur = dbcon.cursor()
        dbcur.execute(sql)
        if dbcur.fetchone()[0] == 1:
            return True
        return False
    except Exception as e:
        print(e)
        return False