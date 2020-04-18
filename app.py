import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1)
    if output < 24 :
        return render_template('index.html', prediction_text='Your chances of having Covid , based on parameters shared is : {} %. Please self isolate, as a precautionary measure and visit a doctor if symptoms persist!'.format(output))
    elif output >= 25 and output <50:
       return render_template('index.html', prediction_text='Your chances of having Covid , based on parameters shared is : {} %. Please talk to a doctor on these symptoms!'.format(output))
    elif output >= 50 and output <70:
       return render_template('index.html', prediction_text='Your chances of having Covid , based on parameters shared is : {} %. Please visit nearby hospital for checkup!'.format(output))
    elif output >= 70 and output <90:
       return render_template('index.html', prediction_text='Your chances of having Covid , based on parameters shared is : {} %. Please get tested on high priority!'.format(output))
    elif output >= 90:
       return render_template('index.html', prediction_text='Your chances of having Covid , based on parameters shared is above 90 %. Please inform your local health authorities immediately!')




@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)