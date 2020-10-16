def insertGDPData(dbcon):
    gdpData = [
        ("USA", 20.5),
        ("China", 13.4),
        ("Germany", 4.0),
        ("Japan", 4.9),
        ("France", 2.8),
    ]
    sql = 'INSERT INTO gdp VALUES(%s, %s)'
    try: 
        dbcur = dbcon.cursor()
        dbcur.executemany(sql, gdpData)
        dbcon.commit()
    except Exception as e:
        print(e)
