from flask import Flask
import sqlite3
import pandas as pd

app = Flask(__name__)


import sqlite3
import pandas as pd

df = pd.read_csv('cannabis.csv')
conn = sqlite3.connect('cannabis.sqlite3')
curs = conn.cursor()

drop_table = '''DROP TABLE cannabis;'''
curs.execute(drop_table)

df.to_sql('cannabis', conn)

query1 = '''SELECT * FROM cannabis
WHERE Effects LIKE '%Sleepy%'
  AND Effects LIKE '%Creative%';'''


result_query = curs.execute(query1).fetchall()

@app.route('/')
def hello_world():
    return str(result_query)