import pandas as pd
from file_util import split_cat_dog

def create_symptom_list(filePath,
                        fileName):

    petDisease = pd.read_csv(filePath+fileName, encoding='euc-kr')

    all_words = ['이름']
    for n in range(len(petDisease)):
        text = petDisease['주요증상'].iloc[n]
        text = text.replace('|',',')
        text = text.replace('\r','')
        words = text.split(',')
        for word in words:
            if word not in all_words and len(word) > 0:
                all_words.append(word)

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
