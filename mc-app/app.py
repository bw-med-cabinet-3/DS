from flask import Flask
import sqlite3
import pandas as pd


df = pd.read_csv('cannabis.csv')
conn = sqlite3.connect('cannabis.sqlite3')
curs = conn.cursor()
drop_table = '''DROP TABLE cannabis;'''
curs.execute(drop_table)
df.to_sql('cannabis', conn)

query1 = '''SELECT * from cannabis;'''


result_query = curs.execute(query1).fetchall()


def create_app():
  app = Flask(__name__)
  @app.route('/')
  def hello_world():
    return str(result_query)

  return app


if __name__ == "__main__":
  app = create_app()