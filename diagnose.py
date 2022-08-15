import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import warnings

# PerformanceWarning 출력 안하도록 설정
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

def model_train(name):
    if name != "cat" and name != "dog":
        return None

    filePath = "data/"+name+"/"
    petDisease = pd.read_csv(filePath+'animal_disease.csv', encoding='euc-kr')
    symptomList = pd.read_csv(filePath+'symptomList.csv', encoding='euc-kr')

    all_words = []
    for i in range(len(symptomList)):
        all_words.append(symptomList["이름"].iloc[i])
    print(len(all_words))

    for word in all_words:
        petDisease.insert(3,word,0)
        for i in range(len(petDisease)):
            text = str(petDisease.loc[i, '주요증상'])
            if text.find(word) != -1:
                petDisease.loc[i, word] = 1

    X = petDisease.iloc[:,3:]
    y = petDisease['질병명']

    tree_clf = DecisionTreeClassifier(max_depth=300)
    tree_clf.fit(X, y)

    print("훈련 세트 정확도: {:.3f}".format(tree_clf.score(X, y)))

    pickle.dump(tree_clf, open(filePath+'diagnose.pkl', 'wb'))
    petDisease.to_csv(filePath+"labeledData.csv", index=False, encoding='euc-kr')

if __name__ == "__main__":
    model_train("cat")
    model_train("dog")
