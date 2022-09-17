import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle

from diagnose import load_train_data
from file_util import create_test_data

def model_test(filePath,
               fileName,
               symptomListFileName):

    X, y = create_test_data(filePath, fileName, symptomListFileName)
    model = pickle.load(open(filePath+'diagnose.pkl', 'rb'))
    print("테스트 세트 정확도: {:.3f}".format(model.score(X, y)*100))

    labeled_data = pd.concat([y,X],axis=1)
    labeled_data.to_csv(filePath+"testLabeledData.csv", index=False, encoding='utf-8')

def fine_tune(filePath,
              testfileName,
              trainFileName,
              symptomListFileName):

    # load test dataset
    test_X, test_y = create_test_data(filePath=filePath,
                                      fileName=testfileName,
                                      symptomListFileName=symptomListFileName)

    # load train dataset
    X, y = load_train_data(filePath=filePath,
                           fileName=trainFileName,
                           symptomListFileName=symptomListFileName)

    n_estimators_list = [30, 60, 90, 120, 150, 180]
    min_samples_split_list = [2, 4, 6, 8, 10, 12, 14, 16]
    max_features_list = ['sqrt', 2, 4, 6, 8, 10, 12, 14]
    max_depth_list = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    count = 0
    loop_len = len(n_estimators_list) * len(min_samples_split_list) * len(max_features_list) * len(max_depth_list)
    result = []
    for n_estimators in n_estimators_list:
        for min_samples_split in min_samples_split_list:
            for max_features in max_features_list:
                for max_depth in max_depth_list:
                    tree_clf = RandomForestClassifier(max_depth=max_depth,
                                                      n_estimators=n_estimators,
                                                      max_features=max_features,
                                                      min_samples_split=min_samples_split,
                                                      random_state=13)
                    tree_clf.fit(X, y)
                    result.append([max_depth, n_estimators, max_features, min_samples_split, tree_clf.score(test_X, test_y)*100])

                    print(count,"/",loop_len)
                    count += 1

    result.sort(key=lambda x: (-x[4]))
    print('| max_depth | n_estimators | max_features | min_samples_split | score |')
    print('| --------- | ------------ | ------------ | ----------------- | ----- |')
    for i in range(10):
        print('| ',result[i][0],' | ',result[i][1],' | ',result[i][2],' | ',result[i][3],' | ',result[i][4],' |')
    print()

if __name__ == "__main__":
    model_test(filePath="data/" + "cat" + "/",
               fileName="ml_test.csv",
               symptomListFileName='symptomList.csv')

    model_test(filePath="data/" + "dog" + "/",
               fileName="ml_test.csv",
               symptomListFileName='symptomList.csv')

    # fine_tune(filePath="data/" + "dog" + "/",
    #           testfileName="ml_test.csv",
    #           trainFileName="animal_diseaseV0.csv",
    #           symptomListFileName='symptomList.csv')
    #
    # fine_tune(filePath="data/" + "cat" + "/",
    #           testfileName="ml_test.csv",
    #           trainFileName="animal_diseaseV0.csv",
    #           symptomListFileName='symptomList.csv')

