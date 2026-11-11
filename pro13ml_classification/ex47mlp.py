# MLP란 여러 개의 퍼셉트론 뉴런을 여러 층을 쌓은 다층신경망 구조이다.
# 입력층과 출력층 사이에 하나 이상의 은닉층을 가지고 있는 신경망이다.
# 인접한 두 층의 뉴런 간에는 완전 연결 -> fully connected 된다.

# 실습1) 논리회로 분류
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

feature = np.array([[0,0], [0,1], [1,0], [1,1]])
print(feature)
label = np.array([0,0,0,1])     # and
# label = np.array([0,1,1,1])     # or
# label = np.array([0,1,1,0])      # xor 해결 못함

# max_iter의 추천 횟수는 500 ~ 1000
ml = MLPClassifier(max_iter=500, hidden_layer_sizes=10, 
                solver='adam',      # cost(loss, 손실) 최소화 방식
                learning_rate_init=0.01, verbose=1).fit(feature, label)
print(ml)


