import json
def fetchAllFromGDP(dbcon):
    sql = "Select * from `%s`"
    value ="gdp".replace("\'","")
    try: 
        dbcur = dbcon.cursor()
        dbcur.execute(sql,(value,))
        rows = dbcur.fetchall()
        # for row in rows:
        #     print(row)
        test = json.dumps(rows)
        print(test)
    except Exception as e:
        print(e)