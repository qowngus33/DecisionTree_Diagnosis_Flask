"""
@auther qowngus33
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import pickle

# 학습 데이터 로딩
def load_train_data(filePath,
                    fileName,
                    symptomListFileName):

    # 질병 데이터와 증상 목록 데이터를 불러옴
    petDisease = pd.read_csv(filePath + fileName, encoding='euc-kr')
    symptomList = pd.read_csv(filePath + symptomListFileName, encoding='euc-kr')

    # 증상 목록 리스트 생성
    all_words = []
    for i in range(len(symptomList)):
        all_words.append(symptomList["이름"].iloc[i])
    print(len(all_words))

    # 0으로 초기화 된 배열 생성
    temp_arr = [[0] * len(all_words) for _ in range(len(petDisease))]

    # 원핫인코딩으로 증상을 포함하면 1로 열 값을 바꿈
    for i in range(len(petDisease)):
        for j in range(len(all_words)):
            text = str(petDisease.loc[i, '주요증상'])
            if text.find(all_words[j]) != -1:
                temp_arr[i][j] = 1

    X = pd.DataFrame(temp_arr, columns=all_words)
    y = petDisease['질병명']

    return X, y

# 모델 학습
def model_train(filePath,
                fileName,
                symptomListFileName,
                max_depth_,
                n_estimators_,
                min_samples_split_,
                max_features_):

    # 학습 데이터 로딩
    X, y = load_train_data(filePath, fileName, symptomListFileName)
    tree_clf = RandomForestClassifier(max_depth=max_depth_,
                                      n_estimators=n_estimators_,
                                      min_samples_split = min_samples_split_,
                                      max_features=max_features_,
                                      random_state=13)
    # 모델 학습
    tree_clf.fit(X, y)
    print("훈련 세트 정확도: {:.3f}".format(tree_clf.score(X, y)))

    # 학습이 완료된 모델을 pickle 파일로 저장
    labeledData = pd.concat([y,X],axis=1)
    pickle.dump(tree_clf, open(filePath+'diagnose.pkl', 'wb'))
    labeledData.to_csv(filePath+"labeledData.csv", index=False, encoding='euc-kr')

if __name__ == "__main__":
    model_train(filePath="data/" + "cat" + "/",
                fileName='animal_diseaseV0.csv',
                symptomListFileName='symptomList.csv',
                max_depth_ = 20,
                n_estimators_ = 150,
                min_samples_split_ = 14,
                max_features_ = 2)

    model_train(filePath="data/" + "dog" + "/",
                fileName='animal_diseaseV0.csv',
                symptomListFileName='symptomList.csv',
                max_depth_=30,
                n_estimators_=150,
                min_samples_split_=2,
                max_features_=14)
