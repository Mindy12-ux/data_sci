import numpy as np
import pandas as pd
import scipy.stats as stats

# [one-sample t 검정 : 문제1]  
# 영사기( 프로젝터 )에 사용되는 구형 백열전구의 수명은 250 시간이라고 알려졌다. 
# 한국 연구소에서 수명이 50 시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명 시간 관련 자료를 얻었다. 
# 한국 연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
# 수집된 자료 :  305 280 296 313 287 240 259 266 318 280 325 295 315 278

# 문제 : 새로 개발된 백열전구의 수명은 300시간인가?
# 귀무 가설 : 한국 연구소에서 개발한 백열 전구의 평균 수명은 300시간이다.
# 대립 가설 : 한국 연구소에서 개발한 백열 전구의 평균 수명은 300시간이 아니다.

data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print('표본 크기 : ', len(data))            # 14
print('표본 평균 수명 : ', np.mean(data))   # 289.7857142857143

# 정규성 검정
result = stats.shapiro(data)
print('shapiro result : ', result)  #  pvalue=0.82086 > 0.05 이므로, 정규성을 만족한다.

t_result = stats.ttest_1samp(data, popmean=300)
print('t_result : ',t_result)
# statistic=-1.5564356, pvalue=0.143606254
# 해석 : 유의수준 0.05 < pvalue=0.143606254 이므로, 귀무가설을 채택한다.
# 결론 : 한국 연구소에서 개발한 백열 전구의 평균 수명은 300시간이다.

print('-----------------')
# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. 
# A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.  
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", ""), null인 관찰값은 제거.

# 문제 : 국내 노트북 평균 사용시간인 5.2 시간과 A회사 노트북의 평균 사용 시간 사이에 차이가 있는지 검정.
# 귀무 가설 : A회사 노트북 평균 사용시간은 5.2 시간이다. (국내 평균과 차이가 없다.)
# 대립 가설 : A회사 노트북 평균 사용시간은 5.2 시간이 아니다. (국내 평균과 차이가 있다.)

data2 = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/one_sample.csv')
print(data2.head(5))
print(data2.describe())

# 전처리
print(data2.info())
data2['time'] = data2['time'].replace("     ", "").str.strip()   # 공백 제거
data2['time'] = pd.to_numeric(data2['time'], errors='coerce')    # str을 숫자로 변환
data2 = data2.dropna(subset=['time'])

print('표본 평균 사용 시간 : ', data2['time'].mean())   # 5.556880
print('표본 크기 : ', len(data2))       # 109

# 정규성 검정
result2 = stats.shapiro(data2['time'])
print('time에 대한 shapiro result : ', result2) # pvalue=0.724230

# One sample t-test
t_result2 = stats.ttest_1samp(data2['time'], popmean=5.2)
print(t_result2) 
# statistic=3.94605956, pvalue=0.00014166691
# 해석 : 유의수준 0.05 > pvalue=0.00014166691 이므로, 귀무가설을 기각한다.
# 결론 : A회사 노트북 평균 사용시간은 5.2 시간이 아니다. (국내 평균과 차이가 있다.) 

print('-------------------')
# [one-sample t 검정 : 문제3] 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오. (월별)

# 문제 : 정부는 전국 평균 미용 요금이 15000원이라고 발표했는데, 실제 데이터와 비교해서 검정해보자.
# 귀무가설 : 전국 평균 미용 요금은 15000원이다. (발표가 맞다)
# 대립가설 : 전국 평균 미용 요금은 15000원이 아니다. (발표가 틀리다)

data3 = pd.read_excel('data.xls')
# print(data3.head(5))
# print(data3.describe())

# 데이터 전처리 : Nan 제거
data3 = data3.T
data3.columns = ['미용']
data3 = data3.dropna(subset='미용')

data4 = data3.iloc[2:, :]   # 숫자 데이터만 추출
data4 = pd.to_numeric(data4['미용'], errors='coerce')
data4.columns = ['미용']
print(data4)
# print(data3.loc[['서울']]) 행을 기준으로 데이터를 추출하고 싶으면 loc['행이름']을 써야함.

# 정규성 검정
result3 = stats.shapiro(data4)  # data4는 series이므로 칼럼명이 존재하지 않음
print('result : ', result3)
# pvalue=0.374694290 > 0.05 이므로 정규성을 만족한다.

# t-검정
t_result3 = stats.ttest_1samp(data4, popmean=15000)
print('t_result : ', t_result3)
# statistic=7.4966452, pvalue=1.8990407726371975e-06
# 해석 : 유의수준 0.05 > pvalue=1.8990407726371975e-06 이므로, 귀무가설을 기각한다.
# 결론 : 전국 평균 미용 요금은 15000원이 아니다. (발표가 틀리다)

