"""
@auther qowngus33
"""
import pandas as pd
from file_util import split_cat_dog

# 증상 목록 열을 생성
def create_symptom_list(filePath,
                        fileName):

    petDisease = pd.read_csv(filePath+fileName, encoding='euc-kr')

    all_words = ['이름']
    for n in range(len(petDisease)):
        text = petDisease['주요증상'].iloc[n]

        # 기본 전처리
        text = text.replace('|',',')
        text = text.replace('\r','')
        words = text.split(',')

        for word in words:
            if word not in all_words and len(word) > 0:
                all_words.append(word)

    # csv 파일로 저장
    symptomList = pd.Series(all_words)
    fileName = filePath + "symptomList.csv"
    symptomList.to_csv(fileName, index = False, encoding="euc-kr")

if __name__ == "__main__":
    split_cat_dog(filePath='data/',
                  fileName="animal_diseaseV0.csv",
                  encoding='euc-kr')

    create_symptom_list(filePath="data/cat/",
                        fileName="animal_diseaseV0.csv")

    create_symptom_list(filePath="data/dog/",
                        fileName="animal_diseaseV0.csv")
