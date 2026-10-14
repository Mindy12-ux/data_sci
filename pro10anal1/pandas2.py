# 재색인 (순서 재배치)
from pandas import Series, DataFrame

# Series의 재색인
data = Series([1,2,3], index=(1, 4, 2))
print(data)     # 1    1 / 4    2 / 2    3
data2 = data.reindex((1,2,4))
# data2 = data.reindex((2, 1, 4)) # 내가 지정한 인덱스 순서대로 재배치
print(data2)    # 1    1 / 2    3 / 4    2 , 인덱스-value 쌍은 유지된 채 순서만 바뀜

print('\n재색인할 때 값 채워넣기')
data3 = data2.reindex([0,1,2,3,4,5])    # 인덱스에 대응된 값이 없으면 NaN
print(data3)

# 대응값이 없는 인덱스에 특정 값으로 채우기
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)    # fill_value : NaN인 곳 값 채워주기
print(data3)

print()
# NaN 앞 값으로 Nan을 채우기
data3 = data2.reindex([0,1,2,3,4,5], method='ffill')    # data2는 정렬된 상태여야 한다
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='pad')    # data2는 정렬된 상태여야 한다
print(data3)

print()
# NaN 뒤(다음) 값으로 Nan을 채우기
data3 = data2.reindex([0,1,2,3,4,5], method='bfill')
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='backfill')
print(data3)

import numpy as np
print('\nDataframe : bool 처리')
df = DataFrame(np.arange(12).reshape(4,3), 
            index=['1월', '2월', '3월','4월'], columns=['강남','강북','서초'])
print(df)   # 데이터 프레임의 열 단위는 시리즈이므로, 하나의 열의 요소는 데이터 타입이 일치해야 한다.

print(df['강남'])           # 해당 열 출력
print(df['강남'] > 3)       # True, False 출력
print(df[df['강남'] > 3])   # 조건이 참인 행만 출력
print()
print(df < 3)   # 전체 자료에 대한 bool 값 출력
df[df<3] = 0    # 3 미만 자료는 0으로 치환
print(df)       # 자료가 바뀌어 있음

print()
# 슬라이싱 관련 메소드
# df.loc['행(열)이름'] : 해당 행(열), df.iloc[행(열)번호] : 위치 기준 행(열)
print(df.loc['3월'])    # 3월 행만 출력
print(df.loc['3월',:])  # 위와 동일
print(df.loc[:'2월'])   # 1월, 2월 행이 출력됨(2월 이하 행), 일반 숫자 슬라이싱과 다르게 '2월' 행까지 모두 출력됨
print(df.loc[:'2월', ['서초']]) # 2월 이하 행의 '서초'열만 출력

print()
print(df.iloc[2])       # 인덱스가 2인 행(3월)
print(df.iloc[2,:])
print()
print(df.iloc[:3])      # 3행 미만 행 3행은 미포함
print(df.iloc[:3,2])    # 3행 미만 행 2열
print(df.iloc[:3, 1:3]) # 3행 미만 행 1,2열
print(df.iloc[1:3, 1:3]) # 1,2행 1,2열





