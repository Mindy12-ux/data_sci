# 고수준의 자료구소(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 ... 등을 제공
# 데이터 랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능
# 데이터 랭글링 / 데이터 먼징 : 가공되지 않은 원시 데이터를 정리, 변환, 구조화하는 과정

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series : 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다.
obj = pd.Series([3, 7, -5, 4, '일'])  # 시리즈 안에 넣을 수 있는 자료구조 - (3, 7, -5, 4) : 가능, {3, 7, -5, 4} : 불가능, dict :가능
print(obj, type(obj))   # dtype: objec, 요소 값이 모두 object type이 된다.
print()

obj = pd.Series([3, 7, -5, 4])
obj2 = pd.Series([3,7,-5,4], index=['a', 'b', 'c', 'd'])
print(obj2)
print(obj2.sum(),' ', np.sum(obj2),' ',sum(obj2))   # 9   9   9
print(obj2.std())   # 5.123475382979799, pandas의 함수는 numpy 기반이다.

print(obj2.index)   # 색인만 출력
print(obj2.values)   # 값만 출력, values의 return 값은 list

# 인덱싱 / 슬라이싱
print(obj2['a'])    # 3 - 'a' 인덱스의 값만 출력 
print(obj2[['a']])  # a    3 - 'a'의 인덱스과 값 모두 출력

print(obj2[['a', 'b']])    # a  3 / b  7
print(obj2['a':'c'])       # a  3 / b  7 / c  5

print()
# print(obj2[2])        # KeyError : 인덱스 순서는 문자열을 사용중
print(obj2.iloc[2])     # iloc[위치번호] : Series의 2번째 위치에 있는 값을 의미
print(obj2.loc['c'])    # loc['인덱스 이름']

print()
print(obj[1:4])
print(obj[[2,1]])   # obj2로 실습하면 에러가 남. obj2에 이미 문자 인덱스를 부여했기 때문.
print(obj.iloc[[2,1]])  # 위치 기반 : 2번 1번 순서대로 출력 /  [] 대괄호 한 개 : value값만 출력 , [[]] 대괄호 두 개 : 인덱스까지 함께 출력 
print(obj.iloc[[1,2]])

print()
print('a' in obj2)  # 인덱스에 해당 값이 있는지 확인
print('k' in obj2)

print('\n파이썬 dict 자료를 Series 객체로 생성')
names = {'mouse':5000, 'keyboard':35000, 'monitor':550000}
print(names, type(names))

obj3 = Series(names)
print(obj3, type(obj3))     # dict의 key가 인덱스로, value가 value 값으로 들어감.
obj3.index = ['마우스', '키보드', '모니터']
print(obj3)

obj3.name = '상품가격'
print(obj3)

print('------------------')
'''
DataFrame : 
표모양(2차원형태자료)의 자료 구조로 여러 개의 칼럼을 갖는다. (Series가 모인 형태)
각 칼럼은 서로 다른 종류의 값을 기억할 수 있다. 
같은 길이의 리스트에 담긴 dicttype의 데이터를 이용해 DataFrame 객체 생성. 
'''

df = pd.DataFrame(obj3)
print(df, type(df))

print()
data = {
'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
'nai':[23, 25, 33, 30, 35],
}
frame = pd.DataFrame(data)   # dict -> DataFrame
print(frame)

print()
print(frame['irum'], type(frame['irum']))   # 데이터프레임에서 '이름' 열만 추출
print(frame.irum, type(frame.irum))         # 위와 결과 동일

print(DataFrame(data=data, columns=['juso', 'irum', 'nai']))    # 열(column) 순서 변경

# NaN (Not a Number 결측치, 값이 없거나 알 수 없는 Missing Value를 의미함)
frame2 = pd.DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'],
                    index=['a', 'b', 'c', 'd', 'e'])
print(frame2)   # tel 열이 NaN으로 찍힘

frame2['tel'] = '111-1111'
print(frame2)

print()
val = pd.Series(['222-2222', '333-3333', '444-4444'], index=['b', 'c', 'e'])
print(val)

print()
frame2['tel'] = val   # 기존 자료 덮어쓰기
print(frame2)

print()
print(frame2.T)     # 행과 열의 전치

print()
print(frame2.values, type(frame2.values))   # 데이터베이스의 값만 꺼냄, 타입 : numpy.ndarray
print(frame2.values[0,1])
print(frame2.values[0:2])

print()
# 삭제
#frame3 = frame2.drop('d')   # 행 삭제
frame3 = frame2.drop('d', axis=0)   # 확실하게 행을 명시
print(frame3)

frame4 = frame2.drop('tel', axis=1)  # 열 삭제
print(frame4)                        # 엄밀히 이야기하면 복사본이 만들어진 것, 원본은 그대로 남아있음

print('-----------------')
print(frame2)
print(frame2.sort_index(axis=0, ascending=False))   # 행 단위 정렬
print(frame2.sort_index(axis=1, ascending=True))    # 열 단위 정렬
print()
print(frame2.rank(axis=0))  # 순위를 매김.
'''
a   5.0  1.0   4.0  NaN
b   4.0  2.0   1.0  1.0
c   2.0  4.0   4.0  2.0
d   1.0  3.0   4.0  NaN
e   3.0  5.0   2.0  3.0
'''

counts = frame2['juso'].value_counts()
print(counts)

# 문자열 자르기
data = {
    'juso':['서초구 서초2동', '강남구 역삼동',  '강남구 대치동'],
    'inwon':[23,25,15]
}
fr = pd.DataFrame(data)
print(fr)

# result1 = Series(x.split()[0] for x in fr.juso)
# result2 = Series(x.split()[1] for x in fr.juso)
# print(result1)
# print(result2)
# print(result1.value_counts())