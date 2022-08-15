import pandas as pd

def split_cat_dog():
    # 데이터프레임을 읽어온 후 기본 전처리
    petDisease = pd.read_csv('data/animal_diseaseV0.csv', encoding='euc-kr')
    petDisease = petDisease.dropna(subset=['질병명'])
    petDisease = petDisease.dropna(subset=['주요증상'])
    petDisease = petDisease.reset_index(drop=True)
    petDisease['주요증상'] = petDisease['주요증상'].str.replace(" ", "")

    # 개, 고양이 파일 분리
    petDiseaseDog = petDisease.loc[petDisease.index[petDisease['축종'].str.contains('개')].tolist(), :]
    petDiseaseDog.to_csv('data/dog/animal_disease.csv', index=False, encoding="euc-kr")

    petDiseaseCat = petDisease.loc[petDisease.index[petDisease['축종'].str.contains('고양이')].tolist(), :]
    petDiseaseCat.to_csv('data/cat/animal_disease.csv', index=False, encoding="euc-kr")


def create_symptom_list(name):
    if name != "cat" and name != "dog":
        return None

    fileName = "data/"+name+"/"+"animal_disease.csv"
    petDisease = pd.read_csv(fileName, encoding='euc-kr')

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
    fileName = "data/" + name + "/" + "symptomList.csv"
    symptomList.to_csv(fileName, index = False, encoding="euc-kr")

if __name__ == "__main__":
    split_cat_dog()
    create_symptom_list("cat")
    create_symptom_list("dog")
