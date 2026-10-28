# 분산(Variance) : 한 개의 변수가 평균으로부터 얼마나 떨어져있는지를 나타낸다.
#                  변수가 하나인 경우에는 분산은 거리과 관계있다.

# 공분산(Covariance) : 두 개의 변수가 함께 어떻게 변화하는지를 나타낸다. 
#   두 변수가 각각의 평균을 기준으로 함께 증가하거나 감소하는 경향이 있는지 나타내는 통계량
#   계산 : 각 관측값이 평균보다 높은지 낮은지를 비교하여 두 편차의 곱을 계산한다.
#   Cov(X,Y)=E{(X−μx)(Y−μy)}
#   변수가 두 개인 경우는 분산은 방향을 가진다.

import numpy as np

# 공분산 : 두 변수의 관계에 대한 방향을 알 수 있다.
print('변수 1 : ', np.arange(1, 6)) 
print('변수 2 : ', np.arange(2, 7)) 
print(np.cov(np.arange(1, 6), np.arange(2, 7))) # 2.5 우상향
print(np.cov(np.arange(10, 60, 10), np.arange(20, 70, 10))) # 250 우상향
print(np.cov(np.arange(100, 600, 100), np.arange(200, 700, 100))) # 25000 우상향
print(np.cov(np.arange(1, 6), (3,3,3,3,3))) # 0 수평선
print(np.cov(np.arange(1, 6), np.arange(6, 1, -1)))# -2.5 우하향
# 두 변수 사이의 선형관계의 방향은 알 수 있으나, 강도를 알 수는 없다.

print()
# 상관계수 : 공분산을 표준화한 값 -> 공분산을 두 변수의 표준편차곱으로 나눈 값
#           두 변수의 측정단위나 크기에 상관없이 -1 ~ 1 사이의 값으로 표시된다.  

x = [8, 3, 6, 6, 9, 4, 3, 9, 3, 4]
print('x 평균 : ', np.mean(x))
print('x 분산 : ', np.var(x))

y = [6, 2, 4, 6, 9, 5, 1, 8, 4, 5]
print('y 평균 : ', np.mean(y))
print('y 분산 : ', np.var(y))

import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
plt.show()

print('x, y의 공분산 : ', np.cov(x, y)) # 대각선에 있는 값이 공분산임.
print('x, y의 공분산 : ', np.cov(x, y)[0,1])    # 5.222222, 두 변수에는 양의 관계가 있다(우상향)

x2 = [80, 30, 60, 60, 90, 40, 30, 90, 30, 40]
y2 = [60, 20, 40, 60, 90, 50, 10, 80, 40, 50]
print('x2, y2의 공분산 : ', np.cov(x2, y2)[0,1])    #  522.22222, 두 변수에는 양의 관계가 있다(우상향) 
plt.plot(x2, y2, 'o')
plt.show()

print()
# 패턴이 일치할지라도 두 데이터의 단위에 따라 공분산의 크기가 달라지므로 절대적 크기 판단이 어렵다.
# 공분산을 표준화해서 -1 ~ 0 ~ 1 범위로 만든 것이 상관계수(r)이다.

print('x, y의 상관계수 : ', np.corrcoef(x, y))
print('x, y의 상관계수 : ', np.corrcoef(x, y)[0,1])     # 0.866368
print('x2, y2의 상관계수 : ', np.corrcoef(x2, y2)[0,1]) # 0.866368

# 피어슨 상관계수(연속형 데이터), 스피어만 상관계수(서열형 데이터), 켄달의 타우

from scipy import stats
print('scipy 모듈을 사용하여 상관계수 r확인 : ', stats.pearsonr(x,y))   # 0.866368
print(stats.spearmanr(x,y))

print('참고 : 비선형 데이터인 경우 공분산, 상관계수는 의미가 없다. -----')
m = [-3, -2, -1, 0, 1, 2, 3]
n = [9, 4, 1, 0, 1, 4, 9]
plt.plot(m, n, 'o')
plt.show()
print(np.cov(m, n)[0,1])        # 0 
print(np.corrcoef(m, n)[0,1])   # 0, 두 데이터가 비선형 관계이기 때문에 상관계수 0 

