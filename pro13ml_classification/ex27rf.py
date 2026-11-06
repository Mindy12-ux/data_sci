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

# 모델 생성
model = RandomForestClassifier(criterion='gini', n_estimators=500, random_state=12)
# criterion='entropy'도 가능, n_estimators(DecisionTree의 개수)=100이 기본
print(model)    # RandomForestClassifier(n_estimators=500, random_state=12
model.fit(train_x, train_y)

pred = model.predict(test_x)
print('예측값 : ', pred[:5])
print('실제값 : ', np.array(test_y[:5]))
print('맞춘 개수 : ', sum(test_y == pred))
print('전체 대비 맞춘 비율 : ', sum(test_y == pred) / len(test_y))
print('분류 정확도 : ', accuracy_score(test_y, pred))   # 0.8279

# 교차 검증 (KFold)
cross_vali = cross_val_score(model, df_x, df_y, cv=5)
print(cross_vali)
print('교차 검증 평균 정확도 : ', np.round(np.mean(cross_vali), 4))   # 0.8082

# RandomForestClassifier는 중요 변수를 제공한다.
print('중요 변수 확인하기 --- ')
print('특성(변수, feature) 중요도 : ', model.feature_importances_)  #  [0.16172779 0.49842824 0.33984396]
# feature_importances_ : 각 feature가 예측에 기여한 정도(중도요)를 수치로 반환
# 중요도 값의 합은 1.0, 수치가 클수록 해당 변수가 불순도 감소에 더 많이 기여한다.
# 수치는 독립변수 열 순서와 동일('Pclass', 'Age', 'Sex')

# 시각화
import matplotlib.pyplot as plt
import koreanize_matplotlib

n_features = df_x.shape[1]
plt.barh(range(n_features), model.feature_importances_, align='center')
plt.xlabel('변수별 중요도 점수')
plt.ylabel('독립 변수')
plt.yticks(np.arange(n_features), df_x.columns)     # 열 이름 표시
plt.show()
plt.close()

print('\n전체 변수를 대상으로 중요도 확인')
# Ticket, Cabin, Embarked : 문자형, 바로 사용 불가(Encoding 해야됨)
# PassengerId, Name : Survived와 상관이 없음

df_imsi = df[['Pclass', 'Age', 'Sex', 'Fare', 'SibSp', 'Parch']].copy()
df_imsi['Sex'] = df_imsi['Sex'].astype('object')  
df_imsi['Sex'] = encoder.fit_transform(df_imsi['Sex'])
train_x, test_x, train_y, test_y = train_test_split(df_imsi, df_y, test_size=0.3, random_state=12)
model.fit(train_x, train_y)

importances = model.feature_importances_

# 칼럼명 + 중요도
feature_df = pd.DataFrame({
    'feature':df_imsi.columns,
    'importance':importances
}).sort_values(by='importance', ascending=False)
print(feature_df)
#   feature  importance
# 1     Age    0.292984
# 3    Fare    0.276886
# 2     Sex    0.241788
# 0  Pclass    0.090802
# 4   SibSp    0.057529
# 5   Parch    0.040012

# 시각화
import seaborn as sns

plt.figure(figsize=(8,5))
sns.barplot(x='importance', y='feature', data=feature_df, orient='h')
plt.xlabel('변수별 중요도 점수')
plt.ylabel('독립 변수')
plt.show()
plt.close()

