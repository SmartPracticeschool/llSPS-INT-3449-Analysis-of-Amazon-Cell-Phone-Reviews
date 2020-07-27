from flask import Flask,request,render_template,jsonify
# from keras.models import load_model
import numpy as np
# import tensorflow as tf
# global model,graph
import pickle
# graph=tf.get_default_graph()
model=pickle.load(open('NLPproject.h5py','rb'))
app=Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/y_pred',methods=['POST'])
def y_pred():
	x_test=[[int(x) for x in request.form.values()]]
	prediction=model.predict(x_test)
	print(prediction)
	output=prediction[0][0]
	return render_template('index.html',
		prediction_text=
		'The review is {}'.format(output))

if __name__=="__main__":
	app.run(debug=True)
