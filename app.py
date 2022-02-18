from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('disease.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("disease.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)

    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1
    s = listToString(prediction)
    print(s)
    return render_template('disease.html', pred='You might have following disease : {}'.format(s), bhai="Disease")


if __name__ == '__main__':
    app.run(debug=True)
