import duckdb as ddb
import pandas as pd

conn = ddb.connect('sampledb.db')
cur = conn.cursor()

cur.execute("create table if not exists person (id INT, name TEXT);")

cur.execute("insert into person values (1, 'John');")

conn.commit()

cur.close()
conn.close()

"""

import duckdb as ddb
or u can use
ddb.read_csv()

res = ddb.sql('select * from df;')

res.fetchall()

res.df()

ddb.commit()

ddb.close()


conn = ddb.connect('sampledb.ddb')



"""