from flask import Flask
import sqlite3
import pandas as pd


def create_app():
  app = Flask(__name__)
  @app.route('/')
  def hello_world():
    return 'Hello world'

  return app


if __name__ == "__main__":
  app = create_app()