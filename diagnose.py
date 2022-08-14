import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import warnings

# PerformanceWarning 출력 안하도록 설정
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# 데이터프레임을 읽어온 후 기본 전처리
petDisease = pd.read_csv('animal_diseaseV0.csv', encoding='euc-kr')
petDisease = petDisease.dropna(subset=['질병명'])
petDisease = petDisease.dropna(subset=['주요증상'])
petDisease = petDisease.reset_index(drop=True)
petDisease['주요증상'] = petDisease['주요증상'].str.replace(" ","")

all_words = []
symptomList = pd.read_csv('symptomList.csv', encoding='euc-kr')
print(symptomList.dtypes)

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

pickle.dump(tree_clf, open('diagnose.pkl', 'wb'))
petDisease.to_csv("labeledData.csv", index=False, encoding='euc-kr')
