# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

# 데이터 준비
dataset = pd.read_csv('winequality-red.csv')
print(dataset.head(3))
print(dataset.info())
print(dataset.shape)
print(dataset.isnull().any())

columns = dataset.columns
# ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
#    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
#    'pH', 'sulphates', 'alcohol', 'quality']

df_x = dataset[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol']]
df_y = dataset['quality']

print(df_x.head(2))
print(df_y.head(2))

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3, random_state=12)

# 모델 생성
model = RandomForestClassifier(criterion='gini', n_estimators=500, random_state=12)
model.fit(x_train, y_train)

pred = model.predict(x_test)
print('예측값 : ', pred[:5])
print('실제값 : ', np.array(y_test[:5]))
print(f'맞춘 개수 / 전체 개수 : {sum(y_test == pred)} / {len(y_test)}')
print('분류 정확도 : ', accuracy_score(y_test, pred))

# 교차 검증(KFold)
cross_vali = cross_val_score(model, df_x, df_y, cv=5)
print('교차검증 정확도 : ', cross_vali)
print('교차 검증 평균 정확도 : ', np.round(np.mean(cross_vali), 4))

# 중요도 확인하기
importances = model.feature_importances_

features_df = pd.DataFrame({
    'feature':df_x.columns,
    'importance':importances
}).sort_values(by='importance', ascending=False)
print('중요도 : \n', features_df)

# 시각화
plt.figure(figsize=(8, 5))
sns.barplot(x='importance', y='feature', data=features_df, orient='h')
plt.xlabel('변수별 중요도 점수')
plt.ylabel('독립 변수')
plt.show()
plt.close()