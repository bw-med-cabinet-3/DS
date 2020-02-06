from flask import Flask, request
import pandas as pd
from mc_app import mc_utils

result = mc_utils.recommend_strains('superman-og', 10)


def create_app():
    app = Flask(__name__)
    @app.route('/')
    def myfunc():
      return str(result)

 
    return app
     



if __name__ == "__main__":
    app = create_app()
