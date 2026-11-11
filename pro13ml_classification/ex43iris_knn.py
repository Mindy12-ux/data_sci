# iris dataset으로 실습
# KNN

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, MinMaxScaler  # 표준화, 정규화

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
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
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
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5) 

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
print(f'test score : {model.score(x_test, y_test)}')
# train score와 test score의 차이가 크면 overfitting 의심

# 학습 후 검증이 끝난 모델을 저장하고 읽기
import joblib
joblib.dump(model, 'ex20model.sav')     # 확장자로 '.model'도 많이 사용
# ------------------------------------------
read_model = joblib.load('ex20model.sav')
print(read_model)   # LogisticRegression(random_state=0)

print('\n새 값으로 예측하기')
new_data = np.array([[5.5, 2.2], [0.8, 0.2],[8.5, 6.7]])
# 주의 : 만약 포준화된 feature로 모델을 생성했다면 new_data도 표준화 해야함.
# sc = StandardScaler()
# sc.fit(new_data)
# new_data = sc.transform(new_data)

new_pred = read_model.predict(new_data)
print('예측 결과 : ', new_pred)              # 예측 결과 :  [2] -> 출력된 2는 '분류 기호 2'가 아니라, 아래 '확률 리스트에서 가장 큰 값의 인덱스'를 반환한 것임.
print(read_model.predict_proba(new_data))   # [[2.29896005e-05 5.60517785e-02 9.43925232e-01]]

# iris dataset 분류 연습용 시각화 코드
import matplotlib.pyplot as plt
import koreanize_matplotlib
from matplotlib.colors import ListedColormap

def plot_decision_regionFunc(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')      # 마커 표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 인자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)   # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프 상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)   
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], color=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_regionFunc(X=x_combined_std, y=y_combined, classifier=read_model, test_idx=range(105, 150), title='scikit-learn제공') 