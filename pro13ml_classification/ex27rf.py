# RandomForest 분류 알고리즘
# 머신러닝에서 분류와 회귀 분석에 널리 사용되는 강력한 앙상블 학습 알고리즘.
# 여러 개의 결정 트리(Decision Tree)를 생성하고, 이들의 예측 결과를 종합하여 최종적인 분류 결과를 도출한다.
# 앙상블 기법 중 배깅을 사용 : 복수의 샘플 데이터와 decision tree를 학습시키고, 결과를 집계하는 방식
# 참고 : 우수한 성능은 Boosting, 과적합이 걱정된다면 Bagging 사용

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

df = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/titanic_data.csv')
print(df.head(3))
print(df.info())
print(df.shape)
print(df.isnull().any())

df = df.dropna(subset=['Pclass', 'Age', 'Sex'])
print(df.shape)

df_x = df[['Pclass', 'Age', 'Sex']].copy()     # feature
# .copy()가 있는 경우 : 원본에서 선택한 데이터를 명시적으로 복사해서 독립적인 DataFrame을 만든다. 따라서 df_x를 수정해도 원본 df의 데이터는 변경되지 않는다.
# 컬럼을 선택해서 새로운 DataFrame을 만들지만, pandas 내부적으로 데이터가 복사되는지, 메모리를 공유하는지는 상황에 따라 달라질 수 있습니다.
# 따라서 df_x를 수정했을 때 원본 df에 영향을 주지 않는다고 무조건 단정하는 것보다는 주의하는 것이 좋습니다.

print(df_x.head(3))
# 전처리 --Sex열(male, female) -> Label Encoding(문자범주형 -> 정수로 변환)
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df_x['Sex'] = df_x['Sex'].astype('object')  # 정수 대입이 가능한 자료형으로 변경
df_x['Sex'] = encoder.fit_transform(df_x['Sex'])
print(df_x.head(3))     # female:0, male:1

df_y = df['Survived']
print(df_y.head(3))     # 1:생존, 2:사망

print()
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.3, random_state=12)





