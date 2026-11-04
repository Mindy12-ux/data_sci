# LogisticRegression : 날씨 예보(비가 올지 안올지 예측)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/weather.csv')
print(data.head(3), data.shape) # (366, 12)
print(data.info())
df = pd.DataFrame()
df = data.drop(['Date', 'RainToday'], axis=1)   # axis=1 : 열 삭제
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes':1, 'No':0})  # yes, no를 1, 0로 매핑
print(df.head(2), df.shape)         # (366, 10)
print(df['RainTomorrow'].unique())  # [1 0]
# RainTomorrow : 종속변수(class) - 범주형, 나머지열 : 독립변수(feature)

print('데이터 분리 : 학습용(train dataset), 검증용(test dataset)')
# 모델의 성능을 객관적으로 파악하기 위함 - 과적합 방지
train, test = train_test_split(df, test_size=0.3, random_state=42)  # random_state=42 : 같은 결과를 얻기 위해 랜덤시드 고정
print(train.shape, test.shape)  # (256, 10) (110, 10)
print(train.head(3))
print(test.head(3))

# 모델 생성
col_select = '+'.join(train.columns.difference(['RainTomorrow']))
print(col_select)
my_formula = 'RainTomorrow ~ '+col_select
model = smf.logit(formula=my_formula, data=train).fit()
print(model.summary())  # 각 변수의 p-value 값이 0.05보다 큰 경우 제거하는 편이 좋음(제거를 고민해봐야 됨)
print(model.params)
print()
print('예측값 : ', np.rint(model.predict(test)[:5].values))
print('실제값 : ', test['RainTomorrow'][:5].values)

# 분류 정확도
# logit에서 제공하는 pred_table : 기본적으로 모델 학습에 사용한 train 데이터만 대상으로 혼동행렬을 생성
pred_mat = model.pred_table()
print(pred_mat)
print('분류 정확도(Accuracy) : ', (pred_mat[0][0] + pred_mat [1,1]) / len(train))   # 0.87109

# test 값으로 confusion matrix를 만들고 싶으면 confusion_matrix 모듈을 사용해야 됨.
from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(test)
conf_mat = confusion_matrix(test['RainTomorrow'], np.rint(pred))
print(conf_mat)
print('분류 정확도(Accuracy) : ', (conf_mat[0][0] + conf_mat [1,1]) / len(test))  #  0.87272
print('분류 정확도(Accuracy) : ', accuracy_score(test['RainTomorrow'], np.rint(pred)))
print('분류 정확도(Accuracy) : ', accuracy_score(test['RainTomorrow'], (pred >= 0.5).astype(int)))  # 함수를 사용하지 않고 만들기, true는 1, false는 0으로 매핑됨.

# 참고 : train data의 분류 정확도와 test data의 분류 정확도가 비슷해야 정상적인 모델
# 만약 그 차이가 크면 과적합을 의심하자.

