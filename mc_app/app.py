from flask import Flask, request, jsonify
import pandas as pd
from mc_app import mc_utils
import pickle

pickle_dict = pickle.load(open("marijuana_dict.p", "rb"))


def create_app():
    app = Flask(__name__)
    @app.route('/strain', methods=['GET'])
    def myfunc():
      strain = '100-og' or request.values['strain']
      return jsonify({strain:pickle_dict[strain]})

 
    return app

if __name__ == "__main__":
    app = create_app()
