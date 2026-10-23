# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오 - 이원카이제곱
# 예제파일 : cleanDescriptive.csv
# 칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
# 조건 :  level, pass에 대해 NA가 있는 행은 제외한다.

import pandas as pd
import scipy.stats as stats

# 데이터 가져오기 , 필요한 정보(부모의 학력/ 자녀의 진학여부)만 남긴 데이터프레임 만들기. 둘 중 하나라도 nan이 있으면 해당 행 제와
data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv', usecols=["level", "pass"])
data = data.dropna()
# print(data)

# 교차표 만들기
ctab = pd.crosstab(data['level'], data['pass'])
ctab.index = ['고졸', '대졸', '대학원졸']
ctab.columns =['합격', '실패']
print(ctab)

# 가설
# 귀무 가설 : 부모의 학력 수준과 자녀의 대학 진학 여부는 아무 연관성이 없다.
# 대립 가설 : 부모의 학력 수준과 자녀의 대학 진학에는 유의미한 연관성이 있다. 

# chi2 검증 
chi2, pv, df, exp = stats.chi2_contingency(ctab)
print(f'검정 통계치 : {chi2:.4f}')
print(f'p-value : {pv:.4f}')
print(f'자유도 : {df}')
print(f'기대값 : \n{exp}')

# 판정
# 유의수준(0.05) < p-value(0.2507)이므로 귀무가설은 유지된다.
# 검정통계치(2.7670) < critical value(5.991)
# 부모의 학력 수준과 자녀의 대학 진학 여부 간에는 유의미한 연관성이 없다.
