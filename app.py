#importing required files
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import jsonify,render_template,url_for, redirect

#building flask app using pickle file
app = Flask(__name__)
app.debug = True
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

#landing page of the app
@app.route('/')
def hello():
    return render_template('index.html')

#prediction
@app.route('/predict',methods=['POST'])
def predict():
    #weight = request.args.get('Weight')
    #length1 = request.args.get('Length1')
    #length2 = request.args.get('Length2')
    #length3 = request.args.get('Length3')
    #height = request.args.get('Height')
    #width = request.args.get('Width')
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    #prediction = classifier.predict([[weight,length1, length2, length3, height, width]])
    prediction = classifier.predict(final_features)
    #return "The predicted spieces is " + str(prediction)
    return render_template('index.html', predict_text = 'The predicted spieces is {}'.format(str(prediction)))

#running flask app
if __name__ == '__main__':
    app.run()
