# 최소 제곱 문제를 행렬방정식으로 표현하고, 수치 선형대수 연산을 통해 최적의 회귀계수(W, b) 구하기

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.5, 2.1])

# plt.scatter(x, y)
# plt.grid(True)
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
# 아래 lin.lstsq 함수가 원하는 행렬 구조(데이터 개수, 변수 개수)로 바꾸기 위함 
print(A)

# 본래 데이터를 직선으로 표현하기 위해 선형대수학을 이용해 y = wx + b의 w, b 구하기
import numpy.linalg as lin

weight, bias = lin.lstsq(A, y)[0]   # 최소제곱법 연산
print(weight, ' ', bias)    # 0.96   -0.9899999999999998
print()
# 회귀식 y^ = 0.96 * x -0.9899999999999998 <= y = wx + b
print(0.96 * 0 -0.9899999999999998) # 실제값 : -1,  예측값 : -0.9899999999999998
print(0.96 * 1 -0.9899999999999998) # 실제값 : 0.2, 예측값 : -0.029999999999999805
print(0.96 * 2 -0.9899999999999998) # 실제값 : 0.5, 예측값 : 0.9300000000000002
print(0.96 * 3 -0.9899999999999998) # 실제값 : 2.1, 예측값 : 1.8900000000000001

# plt.scatter(x, y, marker='o', label='실제값')
# plt.plot(x, weight * x + bias, 'r', label='최적화된 직선')
# plt.grid(True)
# plt.show()

# 경험하지 못한 x값에 대한 예측값 y는 얼마인가?
new_x = 7.5
yhat = weight * new_x + bias
print('예측결과 : ', yhat) # 6.20999999, 신빙성있는 추론된 결과로 미래의 의사결정을 위한 참고자료로 사용 가능하다.

print()
new_x = 1.2345678
yhat = weight * new_x + bias
print('예측결과 : ', yhat)  # 0.1951850880

print('----------------------')
# 선형회귀모델 추세식 계산 클래스
class MySimpleLinearRegression:
    def ___init__(self):
        self.w = None
        self.b = None

    def fit(self, x:np.ndarray, y:np.ndarray):
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        # 최소제곱법 공식 적용
        bunja = np.sum((x - x_mean) * (y - y_mean))
        bunmo = np.sum((x - x_mean) ** 2)
        self.w = bunja / bunmo  # 기울기(가중치)

        self.b = y_mean - (self.w * x_mean)   # 절편(편향)

    def predict(self, new_x:np.ndarray):    # 추청된 w, b를 이용해 새로운 독립변수 x에 대한 예측값을 반환한다.
        return self.w * new_x + self.b


# 실행- 임의의 성인 50명의 키, 몸무게 데이터 생성 후 이를 바탕으로 추세선 만들기
np.random.seed(42)
x_height = np.random.normal(175, 5, 50) # 키 (평균, 표준편차, 개수)
y_weight = np.random.normal(70, 10, 50) # 몸무게

print(x_height)
print(y_weight)
print()

# 모델 생성
model = MySimpleLinearRegression()
model.fit(x_height, y_weight)   # 기존 데이터를 이용해 회귀계수 w,b를 학습
print('추정된 w(기울기 또는 가중치) : ', model.w)
print('추정된 b(절편 또는 편향) : ', model.b)
# yhat = 0.20615129092160211 * 키 + 34.33374147658758

print()
y_pred = model.predict(x_height)    # 기존 데이터로 예측값 확인
# 학습된 회귀계수를 이용해 새로운 키에 대한 몸무게를 추정

for u, i, r in zip(x_height, y_weight, y_pred):
    print(f"키 {u:.2f}cm의 실제값 = {i:.2f}, 예측값 ={r:.2f}")

print()
# 새로운 키에 대한 몸무게 예측
new_height = np.array([198])    # 학습 데이터가 ndarray 타입이었기 때문에 새롭게 생성되는 데이터도 같은 형식으로 줌.
new_weight = model.predict(new_height)
print(f'키 {new_height}cm인 경우 몸무게는 대략 {new_weight}kg일 것이다.')

# 시각화
plt.figure(figsize=(9,6))
plt.scatter(x_height, y_weight, color='blue', label='실제 데이터')
x_line = np.linspace(x_height.min(), x_height.max(), 100)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red', linewidth=2, label='회귀직선')
plt.xlabel('키(cm)')
plt.ylabel('몸무게(kg)')
plt.title('키에 따른 몸무게 선형회귀 분석')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()