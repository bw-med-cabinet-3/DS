from flask import Flask, request, jsonify
import pandas as pd
from mc_app import mc_utils
import pickle

pickle_dict = pickle.load(open("marijuana_dict.p", "rb"))


def create_app():
    app = Flask(__name__)
    @app.route('/')
    def myfunc():
      #strain = strain or request.values['strain']
      return jsonify({'strain':pickle_dict['100-og']})

 
    return app

if __name__ == "__main__":
    app = create_app()
