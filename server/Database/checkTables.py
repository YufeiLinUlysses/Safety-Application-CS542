def checkTableExists(dbcon, tableName):
    sql = """
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = %s
            """
    value = tableName.replace('\'', '\'\'')
    try: 
        dbcur = dbcon.cursor()
        dbcur.execute(sql, (value,))
        if dbcur.fetchone()[0] == 1:
            return True
        return False
    except Exception as e:
        print(e)
        return False
