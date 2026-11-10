import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/weather.csv')
print(df.head(3))
print(df.info())

# 전처리 -
df = df.drop('Date', axis=1)
df['Sunshine'] = df['Sunshine'].fillna(df['Sunshine'].mean())

# 범주형 처리
df['RainToday'] = df['RainToday'].map({'Yes':1, 'No':0})
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes':1, 'No':0})
print(df.head(2))

x = df.drop('RainTomorrow', axis=1) # feature
y = df['RainTomorrow']              # label(class)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# NavieBayes 모델 학습
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
# GaussianNB : 연속형 수치 데이터, 정규분포(Gaussian), 키, 몸무게, 온도
# BernoulliNB : 이진 데이터(0,1), 베르누이 분포, 단어 존재 여부
# MultinomialNB : 빈도/횟수 데이터, 다항분포, 단어 등장 횟수

model = GaussianNB()
model.fit(x_train, y_train)

# 예측 및 평가
from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(x_test)
print('분류 정확도 : ', accuracy_score(y_test, pred))              # 0.8783783
print('confusion_metrix :\n', confusion_matrix(y_test, pred))

print('\n교차검증')
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, x, y, cv=5)
print(f'교차 검증에서 각 fold : {scores}, 평균 : {scores.mean()}')  # 평균 : 0.80895

print()     # feature 중요도 분석 - feature가 정규분포를 따른다는 가정하에 클래스별 평균
# GaussianNB의 멤버 theta_ : 각 클래스별 feature 평균을 반환
mean_0 = model.theta_[0]    # RainTomorrow=0 (비 안오는 날 평균)
mean_1 = model.theta_[1]    # RainTomorrow=1 (비 오는 날 평균)

# 각 feature가 '비 오는 날 vs 비 안오는 날'에서 얼마나 차이가 나는가?
importance = np.abs(mean_1 - mean_0)

feat_impo = pd.DataFrame({
    'feature':x.columns, 'importance':importance
}).sort_values(by='importance', ascending=False)
print('feature 중요도')
print(feat_impo)

# importance 시각화
import matplotlib.pyplot as plt
import koreanize_matplotlib
plt.figure()
plt.bar(feat_impo['feature'], feat_impo['importance'])
plt.xlabel('feature')
plt.ylabel('중요도(평균차이)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print('새로운 자료로 예측')
new_data = pd.DataFrame([{
    'MinTemp': 1.3,
    'MaxTemp': 15.0,
    'Rainfall': 0.0,
    'Sunshine': 10.0,
    'WindSpeed': 3.0,
    'Humidity':  40,
    'Pressure': 1000,
    'Cloud': 3,
    'Temp': 20.0,
    'RainToday': 0
}])

new_pred = model.predict(new_data)
print('예측 결과 : ', '비옴' if new_pred == 1 else '비안옴')
print('확률은 ', model.predict_proba(new_data))
