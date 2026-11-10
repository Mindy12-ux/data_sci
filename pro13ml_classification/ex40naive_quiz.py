# [GaussanNB 문제] 
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
# 참고 : from xgboost import plot_importance

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier, plot_importance
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# 데이터 가져오기 
dataset = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/mushrooms.csv')
print(dataset.head(2))
print(dataset.info())

x_df = dataset.drop('class', axis=1)
y_df = dataset['class']

for col in dataset.columns:
    print(f'[{col}]')
    print('고유값:', dataset[col].unique())
    print('고유값 개수:', dataset[col].nunique())
    print()

x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=123)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# X 데이터 인코딩
encoder = OneHotEncoder(handle_unknown='ignore')

x_train_encoded = encoder.fit_transform(x_train)
x_test_encoded = encoder.transform(x_test)

# y 데이터 인코딩
label_encoder = LabelEncoder()

y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# 중요 변수 추출용 xgboost 학습
xgbmodel = XGBClassifier()
xgbmodel.fit(x_train_encoded, y_train_encoded)

# plot_importance로 중요 변수 시각화
# plot_importance(xgbmodel)
# plt.show()

print(x_train_encoded, type(x_train_encoded))
# Coords        Values
#   (0, 2)        1.0
#   (0, 9)        1.0
# --> 희소행렬, (행 위치, 열 위치), 인코딩된 값 
# 희소 행렬은 0이 대부분인 데이터에서 0이 아닌 값만 저장해서 메모리를 절약한다.
# 표시되지 않은 행렬이 있다면, 해당 위치의 값은 0인 것.
# 희소행렬을 배열로 보고 싶다면 toarray()를 쓰면 됨.

print(x_train_encoded.toarray(), type(x_train_encoded.toarray()))   # <class 'numpy.ndarray'>
print(y_train_encoded)

# 데이터를 분석하기 위해 str값을 float값으로 인코딩한다.
# 다만 인코딩된 값이 희소행렬이 될 수 있기 때문에, 모델에 넣기 전, toarray()를 이용해 넘파이 배열로 변환한다.

# 인코딩된 열 이름 추출
feature_names = encoder.get_feature_names_out(x_train.columns)
# 원핫 인코딩을 하는 경우 : 원본 데이터와 인코딩한 데이터의 칼럼명과 개수가 다를 수 있음. 
# 그래서 아래처럼 중요도 데이터 프레임을 만들려는 경우, 인코딩한 데이터의 칼럼명을 추출해서 데이터 프레임으로 만들어야 함. 


# 중요도 상위 10개 변수만 추출
importance = xgbmodel.feature_importances_
importance_df = pd.DataFrame({
    'feature':feature_names,
    'importance':importance
}).sort_values(by='importance', ascending=False)

print(importance_df.head(10))


