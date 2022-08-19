import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import warnings
from symptomList import split_cat_dog

def model_test(filePath,
               testfileName,
               symptomListFileName):

    testFile = pd.read_csv(filePath + testfileName, encoding='utf-8')
    testFile = testFile.fillna(0)

    symptomList = pd.read_csv(filePath + symptomListFileName, encoding='euc-kr')

    all_words = []
    for i in range(len(symptomList)):
        all_words.append(symptomList["이름"].iloc[i])
    print(len(all_words))

    temp_arr = [[0]*len(all_words) for _ in range(len(testFile))]

    wrong_word = []
    for i in range(len(testFile)):
        for j in range(1,12):
            name = "질병"+str(j)
            text = testFile[name][i]
            if text in all_words:
                temp_arr[i][all_words.index(text)] = 1
            elif text != 0:
                wrong_word.append(text)

    print(wrong_word)

    X = pd.DataFrame(temp_arr, columns=all_words)
    y = testFile['질병명']

    model = pickle.load(open(filePath+'diagnose.pkl', 'rb'))
    print("테스트 세트 정확도: {:.3f}".format(model.score(X, y)*100))

    for i in range(len(X)):
        if y[i] == model.predict(X.loc[[i]]):
            print(y[i],i)

    labeled_data = pd.concat([y,X],axis=1)
    labeled_data.to_csv(filePath+"testLabeledData.csv", index=False, encoding='utf-8')

if __name__ == "__main__":
    split_cat_dog(fileName="ml_test.csv",
                  filePath='data/',
                  encoding='utf-8')

    model_test(filePath="data/" + "cat" + "/",
               testfileName="ml_test.csv",
               symptomListFileName='symptomList.csv')

    model_test(filePath="data/" + "dog" + "/",
               testfileName="ml_test.csv",
               symptomListFileName='symptomList.csv')

