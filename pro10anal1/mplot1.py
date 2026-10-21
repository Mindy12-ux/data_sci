# matplotlib : 플로팅 라이브러리. 그래프 작성을 위한 다양한 함수를 지원한다
# 데이터 시각화는 복잡하고 방대한 양의 데이터를 차트, 그래프, 지도 등의
# 시각적 형태로 표현하여 정보를 직관적으로 이해하고 빠른 의사결정을 돕는다.

# 시각화의 중요성 ...

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')  # 한글 깨짐 방지, 이걸 쓰면 음수가 깨짐
plt.rcParams['axes.unicode_minus'] = False  # 음수 깨짐 방지
import koreanize_matplotlib     # 위의 두 줄을 대체할 수 있는 방법

x = ['서울', '인천', '수원']    # 그래프 x축에 값은 사실상 인덱스임, 서울, 인천, 수원이 x축에 표시되는게 아님. 실제로 찍히는 것은 각각의 리스트 번호 0,1,2
y = [5, 3, 7]    # list O
y = (5, 3, 7)    # tuple O
# y = {5, 3, 7}  # set x

# plt.xlabel('지역명')
# plt.ylabel('투자액')
# plt.xlim([-1, 3])   # 축의 min, max 값을 lim으로 지정할 수 있다.
# plt.ylim([0,10])
# plt.yticks(list(range(0, 11, 3)))   # ticks(눈금)을 지정해 줄 수 있다.
# plt.plot(x, y)
# plt.show()

# data = np.arange(1, 11, 2)
# plt.plot(data)  # x축의 구간은 자동 설정
# x = [0,1,2,3,4]
# for a, b in zip(x, data):
#     plt.text(x = a, y = b, s = str(b))
# plt.show()

x = np.arange(10)
y = np.sin(x)
print(x, y)
# plt.plot(x, y)
# plt.plot(x, y, 'bo')    # color, marker 지정. (파란색 점)
plt.plot(x, y, 'go--', linewidth=2, markersize=12)  # 초록색 동그라미, 점선도 표시, marker 사이즈는 크게.
plt.show()

# hold : 복수의 plot으로 여러 개의 차트를 겹쳐 그리는 것.
x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.figure(figsize=(10, 5)) # 그래프의 전체 크기 지정 (w, h)
plt.plot(x, y_sin, 'r') # 선 그래프
plt.scatter(x, y_cos)   # 산점도 그래프
plt.legend(['사인','코사인'])   # 범례
plt.show()

print()
# subplot : 하나의 figure를 여러 개의 Axes(plot)으로 나누가
plt.subplot(2, 1, 1)    # 1행
plt.plot(x, y_sin)
plt.title('sin')
plt.subplot(2, 1, 2)    # 2행
plt.plot(x, y_cos)
plt.title('cos')
plt.show()

print()
irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 90, 100]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bo--')
plt.ylim([50, 100])
plt.title('시험 점수')
plt.legend(['국어', '영어'], loc=4) # loc : 범례의 위치 지정
plt.grid(True)

# 그래프를 이미지 파일로 저장하기
fig = plt.gcf()
plt.show()
fig.savefig('mplot1.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('mplot1.png')
plt.imshow(img)
plt.show()