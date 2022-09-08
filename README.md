# DecisionTree-Diagnosis-Flask

* 한국과학기술정보연구원의 동물 질병 데이터를 사용한 주요 반려동물(고양이/강아지) 질병 예측 머신러닝 api
* Machine learning api for predicting pet (cat/dog) diseases using veterinary public data from the Korea Institute of Science and Technology Information

</br>

## Implementation

* Machine Learning Model: **Random Forests**
* Web Api: **Flask**

</br>

## File information

#### 1. symptomList.py
*  Create `symptomList.csv` file using `animal_diseaseV0.csv`
*  Data in the `주요증상` column in the file `animal_diseaseV0.csv` are separated by ',', '|' and stored in a new row in `symptomList.csv`

#### 2. diagnosys.py
  * Generate data for model learning with `symptomList.csv`
    * `labeledData.csv`
  * Generate model from `labeledData.csv` and save models to pickle files
    * `diagnose.pkl`

#### 3. app.py
 * Use machine learning model from `diagnose.pkl`
 * Deploy machine learning model api with Flask
 * View model demo on web

#### 4. test.py
* Test the model with test datas

#### 5. static/templates
* JavaScript file for model demo on web

</br>


## Other
* csv 파일은 Github Release에 Datasets라는 이름의 태그로 올려져있습니다.
* The csv files are tagged with the name 'Datasets' in the Github release.
  
