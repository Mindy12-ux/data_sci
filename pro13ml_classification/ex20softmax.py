# LogisticRegression - iris dataset을 사용한 다항분류(softmax 함수 사용) 실습 
# 소프트맥스 함수는 인공지능의 다중 클래스 분류 문제에서 출력층에 주로 사용된다.

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, MinMaxScaler  # 표준화, 정규화
from sklearn.linear_model import LogisticRegression

# 정규화 : 데이터를 0 ~ 1사이의 값으로 바꾸는 것, 표준화 : 데이터의 평균을 0, 표준편차를 1로 바꾸는 것
# LogisticRegression : 이항분류뿐만 아니라, 다중 클래스를 지원함.

iris = datasets.load_iris()
print(iris.keys())
print(iris.target)
print(iris.data[:3])
print(np.corrcoef(iris.data[:, 2], iris.data[:, 3])[0,1])

x = iris.data[:, [2,3]] # 꽃잎 length, width
y = iris.target
print(x.shape, y.shape)     # (150, 2) (150,)
print(x[:3], y[:3], set(map(int, y)))   # {0, 1, 2}

print('\ntrain/test split (7:3)')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[:3],x_test[:3], y_train[:3], y_test[:3])

"""
# 스케일링 (데이터 크기 표준화 내지는 정규화 - 모델의 최적화 과정에서 안정성, 수렴속도가 향상된다. 또한 과적합/과소적합 방지 등에 효과가 있다.)
sc = StandardScaler()   # 표준화
sc.fit(x_train)
sc.fit(x_test)  # 주의 : feature만 스케이링에 참여한다.
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])
print(x_test[:3])

# 스케일링 원상복구
ori_x_train = sc.inverse_transform(x_train)
print('원상복구 데이터 : ',ori_x_train[:3])
"""

print('\n분류 모델 생성 ---------')
model = LogisticRegression(random_state=1)
model = LogisticRegression(
    C=1.0,   # 모델에 패널티 적용(L2규제), 숫자값을 조정해가며 정확도를 확인(숫자가 클수록 규제의 강도가 약해짐)
    solver='lbfgs',   # 최적화 알고리즘 방식 중 하나, w와 b를 계산하는 알고리즘, 이젠 multi_class 옵션은 사라지고 이 옵션이 소프트맥스 지원까지 포괄.
    # multi_class='multinomial',  # softmax 지원 - 최근 버전부터 생략
    max_iter=100,   # 최대 반복 횟수
    random_state=0)
print(model)

model.fit(x_train, y_train) # x_train으로 학습

# 분류 예측
y_pred = model.predict(x_test)  # x_test으로 예측
print('예측값 : ', y_pred)
print('실제값  :', y_test)
print(f'총개수:{len(y_test)}, 오류수:{(y_test != y_pred).sum()}')
# 총개수:45, 오류수:1

print(f'\n분류 정확도 : {accuracy_score(y_test, y_pred)}')  # train_test_split(x, y, test_size=0.3, random_state=42)의 random_state값에 따라 달라짐
conf_mat = confusion_matrix(y_test, y_pred)
print('혼동행렬\n', conf_mat)
print('분류 정확도 : ', np.trace(conf_mat) / np.sum(conf_mat))  # np.trace : 행렬의 대각합을 계산하는 함수, 클래스가 다항인 경우에는 이 방법 사용

print(f'train score : {model.score(x_train, y_train)}')
print(f'tets score : {model.score(x_test, y_test)}')
# train score와 test score의 차이가 크면 overfitting 의심

# 학습 후 검증이 끝난 모델을 저장하고 읽기
import joblib
joblib.dump(model, 'ex20model.sav')     # 확장자로 '.model'도 많이 사용

