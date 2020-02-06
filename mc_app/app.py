from flask import Flask, request, jsonify
import pandas as pd
from mc_app import mc_utils


# Unpickle Dicitionary
# my_dict


def create_app():
    app = Flask(__name__)
    @app.route('/strain', methods=['GET'])
    def myfunc():
      #strain = strain or request.values['strain']
      return 'hello world'# jsonify({strain:my_dict[strain]})

 
    return app

if __name__ == "__main__":
    app = create_app()
