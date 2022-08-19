import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

def model_train(filePath,
                fileName,
                symptomListFileName):

    petDisease = pd.read_csv(filePath+fileName, encoding='euc-kr')
    symptomList = pd.read_csv(filePath+symptomListFileName, encoding='euc-kr')

    all_words = []
    for i in range(len(symptomList)):
        all_words.append(symptomList["이름"].iloc[i])
    print(len(all_words))

    temp_arr = [[0] * len(all_words) for _ in range(len(petDisease))]

    for i in range(len(petDisease)):
        for j in range(len(all_words)):
            text = str(petDisease.loc[i, '주요증상'])
            if text.find(all_words[j]) != -1:
                temp_arr[i][j] = 1

    X = pd.DataFrame(temp_arr, columns=all_words)
    y = petDisease['질병명']

    tree_clf = DecisionTreeClassifier(max_depth=170)
    tree_clf.fit(X, y)

    print("훈련 세트 정확도: {:.3f}".format(tree_clf.score(X, y)))

    count_arr = [0 for _ in range(len(X))]
    for i in range(len(X)):
        if y[i] != tree_clf.predict(X.loc[[i]]):
            count = 0
            for j in range(len(temp_arr[i])):
                if temp_arr[i][j] == 1:
                    count += 1
            count_arr[count] += 1
            print(i,y[i],tree_clf.predict(X.loc[[i]]),count)
    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # print(count_arr)

    pickle.dump(tree_clf, open(filePath+'diagnose.pkl', 'wb'))
    petDisease.to_csv(filePath+"labeledData.csv", index=False, encoding='euc-kr')

if __name__ == "__main__":
    model_train(filePath="data/" + "cat" + "/",
                fileName='animal_diseaseV0.csv',
                symptomListFileName='symptomList.csv')

    model_train(filePath="data/" + "dog" + "/",
                fileName='animal_diseaseV0.csv',
                symptomListFileName='symptomList.csv')
