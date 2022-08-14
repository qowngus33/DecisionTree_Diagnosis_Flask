from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('diagnose.pkl', 'rb'))
app = Flask(__name__)
catDisease = pd.read_csv('labeledData.csv', encoding='euc-kr')

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']

    x_pre = catDisease.iloc[[0]]
    columns = catDisease.columns[4:]

    for column in columns:
        x_pre.loc[0, column] = 0

    for column in columns:
        if len(data1) != 0 and column.find(data1) != -1:
            x_pre.loc[0, column] = 1
        elif len(data2) != 0 and column.find(data2) != -1:
            x_pre.loc[0,column] = 1
        elif len(data3) != 0 and column.find(data3) != -1:
            x_pre.loc[0,column] = 1
        elif len(data4) != 0 and column.find(data4) != -1:
            x_pre.loc[0,column] = 1
        else:
            x_pre.loc[0,column] = 0

    x_pre = np.array(x_pre.iloc[0][3:]).reshape(1, -1)
    probability = model.predict_proba(x_pre)
    probability = probability[0].tolist()

    first = 0
    second = 0
    third = 0
    first_idx = 0
    second_idx = 0
    third_idx = 0
    for i in range(len(probability)):
        if probability[i] > first:
            first = probability[i]
            first_idx = i
        elif first > probability[i] > second:
            second = probability[i]
            second_idx = i
        elif second > probability[i] > third:
            third = probability[i]
            third_idx = i

    classes = model.classes_
    return render_template('after.html',
                           data1=classes[first_idx],
                           data2=classes[second_idx],
                           data3=classes[third_idx],
                           proba1=first*100,
                           proba2=second*100,
                           proba3=third*100)

if __name__ == "__main__":
    app.run(debug=True)
