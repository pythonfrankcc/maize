from flask import Flask, request, jsonify
import json
from flask_cors import CORS 
from flask_restful import Resource, Api
import random

import warnings
warnings.filterwarnings("ignore")


app = Flask(__name__)
api = Api(app)
CORS(app)
# app.url_map

#MODEL = pickle.load(open('classification_model.sav', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
	raw_image = request.get_json(force=True)
	our_image = raw_image['image']
	diseases = ['Common Rust', 'Maize streak virus', 'Northblight leaf']
	for x in diseases:
		ourindex = random.randint(0, 2)
		result = diseases[ourindex]
	return jsonify(prediction=result)
if __name__ == '__main__':
    app.run(port = 5000, debug=True)
