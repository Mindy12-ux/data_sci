'''

1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.

cut() 함수 사용

bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]


2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 

df.pivot_table()

index에는 성별(Sex)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.

출력 결과 샘플1 :       

pclass	1	2	3
sex			
female	0.968085	0.921053	0.500000
male	0.368852	0.157407	0.135447

index에는 성별(Sex) 및 나이(Age)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.

출력 결과 샘플2 : 위 결과물에 Age를 추가. 백분율로 표시. 소수 둘째자리까지.    예: 92.86'''

import pandas as pd
import numpy as np

# 데이터 읽기
df = pd.read_csv('titanic.csv')
print(df.head(2))
print(df.columns)   # 칼럼명 확인

print()
# 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산
bins = [1, 20, 35, 60, 150]     # 나이 구간 경계값
labels = ["소년", "청년", "장년", "노년"]

df['나이대'] = pd.cut(df['Age'], bins=bins, labels=labels)  # 나이대를 표시하는 칼럼 하나 표시, 칼럼명:Age
print(df.head(3))

# Survived : 생존:1, 사망:0
# Observed=True, 범주형 데이터로 소계 구할 때 실제 존재하는 나이대만 참여.
# reset_index() : 인덱스로 올라간 값을 일반 칼럼으로 내리기
result = (df.groupby('나이대', observed=True)['Survived'].sum().reset_index())
print(result)   # 나이대에 대한 생존 인원수

result.columns = ['나이대', '생존자수']     # 출력 칼럼명 변경, 'Survived' => '생존자수'로 변경
print("나이대에 대한 생존 인원수 : \n",result)

# 2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
pivot1 = df.pivot_table(
    values='Survived',      # 계산에 사용할 값
    index='Sex',            # 행 기준(성별)
    columns='Pclass',       # 열 기준 : 선실 등급
    aggfunc='mean'          # Survived에 대한 평균
)

print('\n성별 및 선실 등급별 생존율')
print(pivot1)

print()

# 3) 성별 + 나이대 + 선실 등급별 생존율
pivot2 = df.pivot_table(
    values='Survived',        # 계산에 사용할 값
    index=['Sex', '나이대'],   # 행 기준(성별)
    columns='Pclass',         # 열 기준 : 선실 등급
    aggfunc='mean',            # Survived에 대한 평균
    observed=True             # 실제 존재하는 범주만 출력
)

pivot2 = (pivot2 * 100).round(2)        # 생존율을 %로 변환 후 소수 둘째자리까지 출력
print('\n성별 + 나이대 + 선실 등급별 생존율')
pivot2 = pivot2.fillna(0)   # NaN은 0으로 대체
print(pivot2)



