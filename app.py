"""
@auther qowngus33
"""
from flask import Flask, render_template, request
import pickle
import pandas as pd

model_cat = pickle.load(open('data/cat/diagnose.pkl', 'rb'))
model_dog = pickle.load(open('data/dog/diagnose.pkl', 'rb'))

app = Flask(__name__)
catDisease = pd.read_csv('data/cat/labeledData.csv', encoding='euc-kr')
dogDisease = pd.read_csv('data/dog/labeledData.csv', encoding='euc-kr')

global first_diagnosis

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    global first_diagnosis
    first_diagnosis = " "

    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']

    if data1 == "개" or data1 == "강아지" or data1 == "dog" or data1 == "puppy":
        x_pre = dogDisease.iloc[[0]]
        columns = dogDisease.columns[1:]
        model = model_dog
    else:
        x_pre = catDisease.iloc[[0]]
        columns = catDisease.columns[1:]
        model = model_cat

    for column in columns:
        if len(data2) != 0 and column.find(data2) != -1:
            x_pre.loc[0,column] = 1
        elif len(data3) != 0 and column.find(data3) != -1:
            x_pre.loc[0,column] = 1
        elif len(data4) != 0 and column.find(data4) != -1:
            x_pre.loc[0,column] = 1
        else:
            x_pre.loc[0,column] = 0

    x_pre = x_pre.drop(['질병명'], axis=1)
    probability = model.predict_proba(x_pre)
    probability = probability[0].tolist()

    first, second, third = [0,0,0]
    first_idx, second_idx, third_idx = [0,0,0]
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
    first_diagnosis = classes[first_idx]

    return render_template('after.html',
                           data1=classes[first_idx],
                           data2=classes[second_idx],
                           data3=classes[third_idx],
                           proba1=first*100,
                           proba2=second*100,
                           proba3=third*100)

@app.route("/tospring")
def spring():
    return first_diagnosis

if __name__ == "__main__":
    app.run(debug=True)
