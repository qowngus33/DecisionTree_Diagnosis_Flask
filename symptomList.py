import pandas as pd

def split_cat_dog(fileName,
                  filePath,
                  encoding):
    # 데이터프레임을 읽어온 후 기본 전처리
    petDisease = pd.read_csv(filePath+fileName, encoding=encoding)
    petDisease = petDisease.loc[:, ['질병명', '축종', '주요증상']]
    petDisease.drop(['Unnamed: 0'], axis=1, inplace=True)
    petDisease = petDisease.dropna(subset=['축종'])
    petDisease = petDisease.dropna(subset=['주요증상'])
    petDisease = petDisease.dropna(subset=['질병명'])
    petDisease['주요증상'] = petDisease['주요증상'].str.replace(" ", "")

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
