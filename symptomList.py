import pandas as pd
from konlpy.tag import Twitter

# 데이터프레임을 읽어온 후 기본 전처리
petDisease = pd.read_csv('animal_diseaseV0.csv', encoding='euc-kr')
petDisease = petDisease.dropna(subset=['질병명'])
petDisease = petDisease.dropna(subset=['주요증상'])
petDisease = petDisease.reset_index(drop=True)
petDisease['주요증상'] = petDisease['주요증상'].str.replace(" ","")

twt = Twitter()
all_words = []

for n in range(len(petDisease)):
    text = petDisease['주요증상'].iloc[n]
    text = text.replace('|',',')
    text = text.replace('\r','')
    words = text.split(',')
    for word in words:
        if word not in all_words and len(word) > 0:
            all_words.append(word)

new_words = ['이름']
for i in range(len(all_words)):
    word = all_words[i]
    flag = False
    for j in range(i+1,len(all_words)):
        if all_words[j].find(word) != -1:
            flag = True
    if not flag:
        new_words.append(word)

print(len(new_words))

symptomList = pd.Series(new_words)
symptomList.to_csv('symptomList.csv', index = False, encoding="euc-kr")
