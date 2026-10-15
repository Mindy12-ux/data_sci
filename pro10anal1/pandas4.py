# DataFrame의 재구조화 (열을 행으로, 행을 열로 바꾸는 작업)
import numpy as np
import pandas as pd

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), index=['대전', '서울'], columns=['2023', '2024', '2025'])
print(df)

print()
# stack, unstack
df_row = df.stack()     # 열을 아래로 내려서 행 인덱스쪽으로 쌓기 (가로로 펼쳐진 열을 세로로 쌓기)
print(df_row)
print()
df_col = df_row.unstack()   # 행 인덱스를 다시 열쪽으로 펼치기 (세로로 쌓인 인덱스를 다시 가로로 펼치기)
print(df_col)

print('\n범주화 -------------')
price= [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11 ]   # 구간 기준 값 (3개) - (3, 7] (7, 9] (9, 11] 
result_cut = pd.cut(price, cut)     # 연속형 -> 범주형
print(result_cut)   # [(9, 11], (3, 7], (7, 9], (3, 7]]
print()
result_cut = pd.cut(price, bins=cut, labels=['저가', '중가', '고가'])
print(result_cut)
print()
print(pd.Series(result_cut).value_counts())

# pd.qcut() : 데이터 개수가 비슷하도록 분위수 기준 자동 분할

print('--------------')
datas = pd.Series(np.arange(1, 1001))
# print(datas)
print(datas[:5])
print(datas.head(2))
print(datas[:-2])
print(datas.tail(2))

print('\nagg 함수 : 범주의 그룹별 연산')
datas = pd.DataFrame({
    '부서':['개발', '개발', '영업','영업', '인사', '개발'],
    '이름':['길동', '철수', '영희', '민수', '유리', '찬우'],
    '연봉':[4500, 4200, 4000, 4500, 3500, 3900],
    '성과점수':[90, 85, 70, 75, 88, 95]
})
print(datas)

print(datas.groupby('부서')['연봉'].mean())  # 부서별 연봉 평균 구하기
print(datas.groupby('부서')['이름'].count()) # 부서별 건수
print(datas.groupby('부서')[['연봉', '성과점수']].mean()) # 부서별 연봉, 성과점수 평균

pd.set_option('display.max_columns', None)
print(datas.groupby('부서')['연봉'].agg(['sum', 'mean', 'count']))  # 여러 집계 함수를 한 번에 처리

print()
# agg 대신 사용자 함수를 작성

datas = pd.DataFrame({
    '연봉':[4500, 4200, 4000, 4500, 3500, 3900],
    '성과점수':[90, 85, 70, 75, 88, 95]
})


def summaryFunc(gr):
    return {
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min(),
    }

print(datas.apply(summaryFunc)) # apply : 함수 실행용 함수
print()

print('\nmerge : DataFrame 객체 병합 - 공통 칼럼 기준(RDBMS의 join과 유사)')
df1 = pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2':range(3)})
print(df2)
print()
print(pd.merge(df1, df2, on='key')) # 교집합, 양쪽에 모두 존재하는 키만 이용해서 두 데이터 프레임을 merge (sql의 inner join과 유사)
print()
print(pd.merge(df1, df2, on='key', how='inner')) # 교집합 (sql의 inner join과 유사)
print()
print(pd.merge(df1, df2, on='key', how='outer')) # sql의 full outer join과 유사(대응 인자가 없으면 결측치 처리)
print()
print(pd.merge(df1, df2, on='key', how='left')) # 교집합, 양쪽에 모두 존재하는 키만 이용해서 두 데이터 프레임을 merge (sql의 inner join과 유사)
print()
print(pd.merge(df1, df2, on='key', how='right')) # 교집합, 양쪽에 모두 존재하는 키만 이용해서 두 데이터 프레임을 merge (sql의 inner join과 유사)

print()
df3 = pd.DataFrame({'key2':['a', 'b', 'd'], 'data2':range(3)})
print(df3)
print(df1)
print(pd.merge(df1, df3, left_on='key', right_on='key2'))

print()
print('---- concat : 그냥 상하좌우로 붙이기만 함, 공통 칼럼 필요 없음-----')
print(pd.concat([df1, df3], axis=0))    # 행단위, 아래로 붙이기
print()
print(pd.concat([df1, df3], axis=1))    # 열단위, 옆으로 붙이기

print('\nPIVOT 연산 : pivot과 groupby 명령의 중간적 성격')
# pivot : 데이터 열 중에서 두 개의 열(key)을 사용해 데이터의 행렬을 재구성
data = {
    'city':['강남', '강북','강남', '강북'],
    'year':[2000, 2001, 2002, 2002],
    'pop':[3.3, 2.5, 3.0, 2.0]
}
df = pd.DataFrame(data)
print(df)
print(df['pop'].describe())
print()
print(df.pivot_table(index=['city']))   # agggfunc 값을 안주면 기본값이 mean.
print(df.pivot_table(index=['city'], aggfunc='mean'))
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, 'sum']))
print()
print(df.pivot_table(index=['city'], values='pop'))  
print(df.pivot_table(index=['city'], values='pop', aggfunc='mean')) # 위와 상동, 기본 agg가 mean
print(df.pivot_table(index=['city'], values='pop', aggfunc=len))
print()
# pivot tavble을 이요한 구조 재구성 ==> year:행, city:열, pop:계산값
print(df.pivot_table(index=['year'], values='pop', columns=['city']))
print(df.pivot_table(index=['year'], values='pop', columns=['city'], margins=True))
print(df.pivot_table(index=['year'], values='pop', columns=['city'], margins=True, fill_value=0))

print()
hap = df.groupby(['city'])
print(hap.sum())
print(df.groupby(['city']).sum())
print(df.groupby(['city']).mean())



