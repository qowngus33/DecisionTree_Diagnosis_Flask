# DecisionTree-Diagnosis-Flask

### 파일설명

#### 1. symptomList.py
* `animal_diseaseV0.csv` 파일을 통해 `symptomList.csv` 파일 생성
* `symptomList.csv` 파일 내에는 `animal_diseaseV0.csv` 파일 안의 주요증상 열에 있는 데이터를 `,` ,  `|`로 구분하여 새로운 행으로 저장

#### 2. diagnosys.py
  * `symptomList.csv`을 통해 모델 학습용 데이터 생성
    * `labeledData.csv`
  * 생성된 학습용 데이터를 통해 모델을 학습시킨 결과를 pickle 파일 생성 
    * `diagnose.pkl`

#### 3. app.py
 * `diagnosys.py` 에서 생성된 `diagnose.pkl` 파일을 통해 모델 사용
 * Flask를 통한 모델 api 배포
 * 로컬 ip로 웹에서 모델 데모 확인

#### 4. static/templates
* 모델 테스트

#### 5. static/templates
* 웹을 위한 javaScript 파일

</br>

*****

</br>

csv 파일은 Github Release에 Datasets라는 이름의 태그로 올려져있습니다.
  
