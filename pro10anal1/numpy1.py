# numpy의 ndarray는 단순한 배열이라기 보단, 백터/행렬 연산도 가능한 다차원 수치 데이터 구조이다.
# 주요 특징 :
# 동일한 데이터 타입(Homogeneous), 빠른 연산 속도, 메모리 효율성

import numpy as np

ss = ['tom', 'james','oscar', 1, True]  # 파이썬의 리스트 : 여러 타입의 자료로 구성 가능
print(ss, " ", type(ss))    # ['tom', 'james', 'oscar', 1, True] <class 'list'>

ss2 = np.array(ss)  # list type -> ndarray type
print(ss2, " ", type(ss2))  # ['tom' 'james' 'oscar' '1' 'True'] <class 'numpy.ndarray'>
# 상위 type 순서 : bool(가장 순위가 낮음) -> int -> float -> complex -> str(가장 순위가 높음)

# 메모리 비교
li = list(range(1, 10))
print(li)
print(id(li[0]),id(li[1]))  # 140710261679224 140710261679256 : 리스트의 요소는 저장되어 있는 위치가 다름
print(li * 10)  # print(li * 10)은 문자열의 곱하기와 같음(아래 코드 참고). 리스트를 n번 반복하는 결과가 출력됨
print("--" * 10)    

for i in li:
    print(i * 10, end=" ")  # 리스트의 각 요소에 10을 곱하는 코드

print()
num_arr = np.array(li)
print(num_arr[0], " ", num_arr[1], " ", id(num_arr[0]), id(num_arr[1])) # 1   2   1894751002064 1894751002064 : ndarray는 저장된 주소가 동일함
# num_arr[0] : 배열 내부 원소를 읽어서 Numpy scalar 객체로 꺼내온다.

print(num_arr * 10) # [10 20 30 40 50 60 70 80 90]
print()

# b = np.array([1,2,3])
# print(b, b.shape)   # [1 2 3] (3,)

b = np.array([[1,2,3], [4,5,6]])
print(b, b.shape, b.ndim, b.size)   # [[1 2 3] 
                                    #  [4 5 6]] (2, 3), 2(2차원) , 6(사이즈는 6) -> 2행 3열짜리 배열, 2 x 3으로 표현
print(b[0], ' ', b[[0]], " ", b[0,0])   # [1 2 3],  [[1 2 3]]: 2 차원을 유지,  1

print()
# 배열 선언 후 자동으로 값 채우기
c = np.zeros((2,2))
print(c)
d = np.ones((3,3,3))
print(d)
e = np.eye(3)   # 단위 행렬(주대각선은 1, 나머지는 0으로 채운다)
print(e)

print("\n난수 발생")
print(np.random.rand(5))    # 균등 분포 : 0 이상 1 미만의 난수를 발생시킴
print(np.random.randn(5))   # 정규 분포 : 평균이 0, 표준편차가 1인 난수를 발생시킴

np.set_printoptions(threshold=np.inf)   # 출력값이 너무 길면 ...이 나오는데, 이를 무시하고 모든 값을 출력
print(np.mean(np.random.rand(5000)))    # 0.504255468224451 : 평균이 0.5에 근사함
print(np.mean(np.random.randn(5000)))   # -0.008496421793762152 : 평균이 0에 근사함

np.random.seed(0)   # seed : 난수표의 특정 색인 값을 선택해 난수를 고정한다.
print(np.random.randn(2, 3))

print("\n배열의 인덱싱과 슬라이싱")
aa = np.array([1,2,3,4,5])   # 꼭 리스트가 아니어도 됨, tuple, set도 가능, dict는 불가능
print(aa, " ", aa[1])        # 인덱싱 (인덱스는 0부터 시작)
print(aa[1:4])               # 슬라이싱 : 1 이상 4 미만 인덱스에 해당하는 값 출력
print(aa[1:])                # 1 번째부터 끝까지
print(aa[0:5:1])             # [start, end, step (1은 생략 가능)]
print(aa[0:5:2])
print(aa[-2:])               # [4 5]
print(aa[-4:-1])             # [2 3 4]

print()
bb = aa                     # 주소 치환
print(aa)
print(bb)
print(id(aa), ' ', id(bb))  # 주소 동일 : 2507242471856   2507242471856, 하나의 배열을 두 개의 변수가 참조하고 있는 것.
bb[0] = 99
print(bb)
print(aa)                   # 둘 다 [99  2  3  4  5] 출력

cc = np.copy(aa)            # 별도의 복사본 생성
print(id(aa), id(cc))       # 1673938010544 1673938324240
cc[0] = 77
print(aa)                   # [99  2  3  4  5]
print(cc)                   # [77  2  3  4  5]

print("\n2차원 배열의 인덱싱과 슬라이싱")
dd = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print(dd, "\n", dd.shape)   # (3, 4)
print("인덱싱 ---")
print(dd[0])        # [1 2 3 4], 0번째 행의 열 요소값 모두 출력
print(dd[0, 0])
print(dd[2, 3])

print("슬라이싱 --- : dd[행 슬라이싱, 열 슬라이싱]")
print(dd[0][0:3])   # [1 2 3]
print(dd[0:2])      # [[1 2 3 4]
                    #  [5 6 7 8]]
print(dd[1:])       # 1행 이상 모든 행 출력
print(dd[:, 0])     # 모든 행의 0번째 열, [1 5 9]
print(dd[:, 0:2])
print(dd[:, [1]])   # 모든 행의 1번 열을 가져오되, 2차원 형태를 유지 [[ 1  2] [ 5  6] [ 9 10]]
print(dd[1:3, 1:3]) # 1행, 2행의 1열, 2열 출력
print(dd[::])       # 모든 행, 모든 열 출력
print(dd[::2, :])   # 0행, 2행의 모든 열 (행 증가치 2)
print(dd[::2, ::2]) # 0행, 2행의 0열, 2열 출력

print(dd[-1, -1])   # 마지막 행, 마지막 열 값, 12
print(dd[:, -1])    # 모든 행의 마지막 열 출력
print()
print(dd[-1:-4:-1]) # print(dd[::-1]), 행 역순
print(dd[:, ::-1])  # 열 역순

