import pandas as pd

def split_cat_dog(fileName,
                  filePath,
                  encoding):
    # 데이터프레임을 읽어온 후 기본 전처리
    petDisease = pd.read_csv(filePath+fileName, encoding=encoding)

    # 개, 고양이 파일 분리
    petDiseaseDog = petDisease.loc[petDisease.index[petDisease['축종'].str.contains('개')].tolist(), :]
    petDiseaseDog.to_csv(filePath+"dog/"+fileName, index=False, encoding=encoding)

    petDiseaseCat = petDisease.loc[petDisease.index[petDisease['축종'].str.contains('고양이')].tolist(), :]
    petDiseaseCat.to_csv(filePath+"cat/"+fileName, index=False, encoding=encoding)


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

    # new_words = ['이름']
    # for i in range(len(all_words)):
    #     word = all_words[i]
    #     flag = False
    #     for j in range(i+1,len(all_words)):
    #         if all_words[j].find(word) != -1:
    #             flag = True
    #     if not flag:
    #         new_words.append(word)
    #
    # print(len(new_words))

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
