# ROC(Receiver Operating Characteristic) Curve는 모든 분류 임계값에서 분류 모델의 성능을 보여주는 그래프로 X축이 FPR(1-특이도),
# y 축이 TPR(민감도)인 그래프이다.
# 즉, 민감도와 특이도의 관계를 표현한 그래프이다.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=123)
# n_redundant : 독립변수 중 다른 독립변수의 선형조합으로 나타내는 성분 수, 
print(x[:3], x.shape)
print(y[:3], y.shape)

# plt.scatter(x[:,0], x[:,1])
# plt.show()

model = LogisticRegression().fit(x, y)
y_hat = model.predict(x)
print('y_hat : ', y_hat[:10])   # [0 0 0 1 1 1 0 0 0 1]
print('real : ', y[:10])        # [1 0 0 1 0 1 0 1 0 1]


# 모델 성능 파악
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat))
acc = (44 + 44) / 100           # (TP + TN) /전체수 : 정확도
recall = 44 / (44 + 4)          # TP / (TP + FN) : 민감도
precision = 44 / (44 + 8)        #  TP / ( TP + FP) : 정밀도
specificity = 44 / (8 + 44)     # TN / (FP + TN) : 특이도
fallout = 8 / (8 + 44)  # FP / (FP + TN) : 위양성률(fpr)
print('acc : ', acc)
print('recall : ', recall)
print('specificity : ', specificity)
print('precision : ', precision)
print('fallout : ', fallout)
print('fallout : ', 1-specificity)

print()
from sklearn import metrics
acc_score = metrics.accuracy_score(y, y_hat)
print('acc(정확도) : ', acc_score)

cl_rep = metrics.classification_report(y, y_hat)
print('분류모델 성능평가 보고서 : \n', cl_rep)
#        precision    recall  f1-score   support

#    0       0.85      0.92      0.88        48  -> recall : 실제 0인 데이터 48개 중에서 92%를 정확히 분류했다. (원본 데이터의 0이 48개)
#    1       0.92      0.85      0.88        52  -> precision : 모델이 1로 분류한 것 중에 92%가 정확히 맞았다. (원본 데이터의 1이 52개)

# Precision : 예측한 것 중 맞힌 비율 (예측의 정확성)
# Recall    : 실제 정답 중 찾아낸 비율 (정답 탐지 능력)
# F1-score  : Precision과 Recall의 조화평균
# Support   : 실제 클래스별 데이터 개수
# Accuracy  : 전체 데이터 중 올바르게 분류한 비율
# Macro avg : 클래스별 성능의 단순평균
# Weighted avg : 클래스별 데이터 개수를 고려한 가중평균

print()
# ROC Curve의 판별 경계선 설정용 결정함수 데이터 생성
f_value = model.decision_function(x)
print(f_value)
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f', 'y_hat', 'y'])
print(df.head(3))
#-------

fpr, tpr, thresholds, = metrics.roc_curve(y, model.decision_function(x))
# thresholds : 분류결정 임계값 (결정수값)

plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0,1], [0,1], 'k--', label='random classifier line(AUC=0.5)')
# plt.plot([fallout], [recall], 'ro', ms=6)   # 위양성률, 재현률 출력

# 위 명령 대신 특정 임계값에 해당하는 ROX 좌표로 표시
i = 3
plt.plot([fpr[i]], [tpr[i]], 'ro', ms=6, label='선택한 임계값')

plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC Curve')
plt.legend()
plt.show()

print('AUC(Area Under the Curve) : ROC 커브의 밑면적. 1에 근사할수록 좋은 모델이다.')
print('AUC : ', metrics.auc(fpr, tpr))  # 0.95472







