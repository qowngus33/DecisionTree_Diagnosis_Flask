# DecisionTree-Diagnosis-Flask

### 파일설명

#### 1. symptomList.py
* symptomList.csv 파일 생성
* symptomList.csv 파일 내에는 주요증상 열에 있는 데이터를 ',','|'로 구분하여 저장

#### 2. diagnosys.py
  * 모델 학습용 데이터 생성
    * __labeledData.csv__
  * 모델 학습 후 pickle 파일 생성 
    * __diagnose.pkl__

#### 3. app.py
 * diagnosys.py 에서 생성된 pickle 파일을 통해 모델 사용
 * Flask를 통한 모델 api 배포

#### 4. static/templates
* 웹을 위한 javaScript 파일
  
