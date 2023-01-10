from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
app = Flask(__name__,template_folder='templates')
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello():
    return render_template("pre.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)
    if prediction=='high risk':
        return render_template('pre.html',pred='Risky')
    elif prediction=='low risk':
        return render_template('pre.html',pred='Safe')
    else:
        return render_template('pre.html',pred='Take care')
if __name__=="__main__":
    app.run(host='localhost', port=5000)