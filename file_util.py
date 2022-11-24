"""
@auther qowngus33
"""
import pandas as pd

# 테스트 데이터 생성
def create_test_data(filePath,
                     fileName,
                     symptomListFileName):
    testFile = pd.read_csv(filePath + fileName, encoding='utf-8')
    testFile = testFile.fillna(0)
    symptomList = pd.read_csv(filePath + symptomListFileName, encoding='euc-kr')

    # 모든 증상 열을 불러옴
    all_words = []
    for i in range(len(symptomList)):
        all_words.append(symptomList["이름"].iloc[i])
    print(len(all_words))

    temp_arr = [[0] * len(all_words) for _ in range(len(testFile))]

    for i in range(len(testFile)):
        for j in range(1, 12):
            name = "질병" + str(j)
            text = testFile[name][i]
            if text in all_words:
                temp_arr[i][all_words.index(text)] = 1

    X = pd.DataFrame(temp_arr, columns=all_words)
    y = testFile['질병명']

    return X, y

# 축종에 따라 파일을 분리
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
