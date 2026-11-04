# sigmoid function 적용 연습
# LogisticRegression 모델은 wx + b를 logit 변환한 값에 sigmoid function 처리를 한 값을 사용한다.
# log(P/1-P) = wx + b라고 정의된다.
# 그러므로 z = wx + b --> sigmoid(z) --> P(0 ~ 1) : 이항 분류

# sigmoid function 수식에 의해 변환된 값 확인
import math

def sigmoidFunc(num):       # num : logit 변환한 값이라 가정
    return 1 / (1 + math.exp(-num))

print(sigmoidFunc(3))
print(sigmoidFunc(1.5))
print(sigmoidFunc(-5.0))
print(sigmoidFunc(10))
print(sigmoidFunc(0.01))

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

print('\n로짓(logit) 변환된(가정) 값으로 시그모이드 함수 통과 후 결과 시각화')
x = np.linspace(-10, 10, 50)    # 연속형 입력 자료
print(x)

# 선형결합 (이미 logit된 값)
w = 1.5
b = -2
z = w * x + b


def OursigmoidFunc(z):       
    return 1 / (1 + np.exp(-z))

p = OursigmoidFunc(z)
print('p : \n', p)

# 일부만 보기
print('x[:3] : ', np.round(x[:3], 3))           # [-10.     -9.592  -9.184]
print('z[:3](logit) : ', np.round(z[:3], 3))    # [-17.    -16.388 -15.776]
print('p[:3](확률) : ', p[:3])                  # [4.13993755e-08 7.63639448e-08 1.40858451e-07]

# 시각화
plt.figure(figsize=(8,5))
plt.plot(x, p, label='sigmoid(z)', color='blue')
plt.axhline(0.5, color='red', linestyle='--')
plt.axvline(0.5, color='blue', linestyle='--')  # 이건 그냥 내가 궁금해서 그려봄
plt.title('z=wx+b --> sigmoid --> 확률(이항)')
plt.xlabel('x(입력값)')
plt.ylabel('p(확률값)')
plt.grid(True)
plt.legend()
plt.show()