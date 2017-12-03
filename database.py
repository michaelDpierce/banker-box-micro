import logging
from pprint import pprint

import os
import pymysql

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']

conn = pymysql.connect(db_host, db_user, db_pass, db_name)
cur = conn.cursor()

cur.execute("SELECT * FROM users")

results = cur.fetchall()

for r in results:
    print(r)

cur.close()
conn.close()
