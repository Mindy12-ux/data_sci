# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('data.csv')

data = dataset[(dataset['요일'] == '토') | (dataset['요일'] == '일')]
print(data.info())
data = data[['외식유무', '소득수준']]
print(data)

# 1) logit을 사용한 모델 작성
formula = '외식유무 ~ 소득수준'
logit_result = smf.logit(formula=formula, data=data).fit()
print(logit_result.summary())

# 기존 데이터로 예측
pred1 = logit_result.predict(data)
print('예측값 : ', np.around(pred1.values)) 
print('실제값 : ', data['외식유무'].values)

# 모델 정확도 측정
print('수치에 대한 집계표(혼동 행렬)')
conf_tab = logit_result.pred_table()
print(conf_tab)
print('분류 정확도 : ', accuracy_score(data['외식유무'], np.around(pred1)))

# 2) glm을 이용한 모델 작성
glm_result = smf.glm(formula=formula, data=data, family=sm.families.Binomial()).fit()
print(glm_result.summary())

# 기존 데이터로 예측
pred2 = glm_result.predict(data)
print('예측값 : ', np.around(pred2.values)) 
print('실제값 : ', data['외식유무'].values)

# 분류 정확도
print('glm 분류 정확도 : ', accuracy_score(data['외식유무'], np.around(pred2)))

# 키보드로 입력값 받아서 예측하기
logit_value = int(input('소득 수준을 입력하세요 : '))

if not isinstance(logit_value, int) or logit_value < 0:
    print('양의 정수값을 입력하세요')

else:
    # 입력값을 DataFrame으로 변환
    logit_input = pd.DataFrame({'소득수준': [logit_value]})

    # 예측
    logit_pred = logit_result.predict(logit_input)
    if np.round(logit_pred.values) == 1:
        print('새로운 소득수준에 대한 예측 결과 : ', np.around(logit_pred.values))
        print('주말 저녁에 외식을 합니다.')
    else:
        print('주말 저녁에 외식을 하지 않습니다.')