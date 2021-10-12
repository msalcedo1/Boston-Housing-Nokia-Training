# -*- coding: utf-8 -*-
"""
@author: anantSinghCross
"""
import flask
import pickle
#import json
import numpy as np
import pandas as pd
import xgboost
#from sklearn.externals import joblib
from flask import Flask, render_template, request
#from keras.models import model_from_json
from xgboost import XGBRegressor


app = Flask(__name__)

@app.route("/")
@app.route("/AmesHousingIndexindex")
def index():
	return flask.render_template('AmesHousingIndex.html')

@app.route("/predict",methods = ['POST'])
def make_predictions():
    if request.method == 'POST':
        a = request.form.get('GarageCars')
        b = request.form.get('OverallQual')
        c = request.form.get('FullBath')
        d = request.form.get('ExterQual')
        e = request.form.get('GrLivArea')
        f = request.form.get('BsmtQual')
        g = request.form.get('KitchenQual')
        h = request.form.get('TotRmsAbvGrd')
        i = request.form.get('TotalBsmtSF')
        j = request.form.get('CentralAir')
        k = request.form.get('KitchenAbvGr')
		
		X = np.array([[a,b,c,d,e,f,g,h,i,j,k]])

  
        pred = loaded_model.predict(X)
        return flask.render_template('predictPage.html' , response = pred[0])
        
        
if __name__ == '__main__':
    #json_file = open("model.json","r")
	app.run(debug=True, use_reloader=False)
	loaded_model = pickle.load(open("model.dat", "rb"))
    #loaded_model_json = json_file.read()
    #json_file.close()
    #loaded_model = model_from_json(loaded_model_json)
    #loaded_model.load_weights("model.h5")

    app.run(host='0.0.0.0', port=8001, debug=True)
