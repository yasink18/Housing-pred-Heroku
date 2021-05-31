import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math
import re

app = Flask(__name__)
model = pickle.load(open('housing_data.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    result = request.form
    int_features = [int(x) for x in request.form.values()]
    # print(int_features)
    final_features = [np.array(int_features)]
    # print(final_features)
    prediction = float(model.predict(final_features))
    prediction = round(prediction,2)
    return render_template('index.html', prediction='Amount of House would be {}'.format(prediction))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    #
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
   app.run(debug=True)
