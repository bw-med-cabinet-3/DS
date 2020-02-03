import sqlite3
import pandas as pd

df = pd.read_csv('cannabis.csv')
conn = sqlite3.connect('cannabis.sqlite3')
curs = conn.cursor()
df.to_sql('cannabis', conn)

query1 = '''SELECT SUM(character_id)
FROM charactercreator_character;'''


result_query = curs.execute(query1).fetchall())