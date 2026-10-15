# pandas file i/o

import pandas as pd
pd.set_option('display.max_columns', None)  # 모든 칼럼을 표시

df = pd.read_csv('test.csv')
print(df,'\n' ,type(df))
print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex1.csv')
# https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex1.csv
print(df,'\n',type(df))

print()
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex1.csv', sep=',')
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex1.csv', sep=',', skip_blank_lines=True)
# skip_blank_lines=True : 칼럼명, 데이터 앞에 공백 제거
print(df,'\n',type(df))

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv')
print(df)   # 데이터에 명시된 헤더가 없음, 첫 번째 행을 헤더로 사용하고 있음

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None)
print(df)   # header 옵션으로 헤더가 없다는 것을 명시해놓음

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None, skiprows=1)
print(df)

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv', header=None, names=['A','B','C', 'D', 'E'])
print(df)

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt')
print(df, type(df))

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt', sep=r'\s+') # 정규표현식 가능
print(df)

print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt', sep=r'\s+', skiprows=[1,3]) 
print(df)
# skiprows = range(1,3)도 가능, # skiprows = lamdba x:x in [1,3]

print()
# read_fwf : 고정된 문자 폭으로 열 구분, widths로 문자 폭 구분
df = pd.read_fwf('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/data_fwt.txt', header=None, widths=(10,3,5), names=['날짜', '상호', '가격'], encoding='utf8') 
# cp949, euc-kr
print(df)
print(df['날짜'].head(2))

print()
print(df.iloc[:, 0])

print('\n\nChunk : 대량의 데이터를 부분씩(일정 크기) 메모리로 읽어 처리하는 단위')
# 대용량 자료 전체 로딩 시 메모리 초과 오류 발생 방지 - 메모리 관리
# 스트리밍 방식(일부만 순차 처리)으로 읽기, 분산처리의 효과
# 여러 번 반복해서 읽어야하므로, 속도는 느리다.
import time
import numpy as np

n_rows = 100000
data = {
    'id':range(1, n_rows + 1),
    'name':[f'Student_{i}' for i in range(1, n_rows + 1)],
    'score1': np.random.randint(50, 101, size=n_rows),
    'score2': np.random.randint(50, 101, size=n_rows)
}
df = pd.DataFrame(data=data)
print(df.head())
print(df.tail())
csv_fname = 'pandas5student.csv'
# df.to_clipboard()
df.to_csv(csv_fname, index=False)   # DataFrame을 파일로 저장

print('----------')
# csv 파일 읽기 : 전체 한 번에 읽기
start_all = time.time()
df_all = pd.read_csv(csv_fname)
average_all_1 = df_all['score1'].mean()
average_all_2 = df_all['score2'].mean()
time_all = time.time() - start_all
print(f'전체 처리 score1 평균 : {average_all_1:3f}')
print(f'전체 처리 score1 평균 : {average_all_2:3f}')

# Chunk로 읽기
chunk_size = 1000
total_score1 = 0
total_score2 = 0
total_count = 0

start_chunk_total = time.time()
for i, chunk in enumerate(pd.read_csv(csv_fname, chunksize=chunk_size)):
    start_chunk = time.time()

    # 청크 처리 중 첫번째 학생 정보 출력
    frist_student = chunk.iloc[0]
    print(f"chunk {i + 1} 첫번째 학생:ID={frist_student['id']}, \
        이름={frist_student['name']}, score1={frist_student['score1']}, score2={frist_student['score2']}")

    total_score1 += chunk['score1'].sum()
    total_score2 += chunk['score2'].sum()
    total_count += len(chunk)

    end_chunk = time.time()
    elasped = end_chunk - start_chunk
    print(f'    처리 시간 : {elasped:7f}')  # 청크 단위 처리 시간

time_chunk_total = time.time() - start_chunk_total
average_chunk1 = total_score1 / total_count
average_chunk2 = total_count / total_count

print('\n처리 결과')
print(f"""전체 학생 수 :{total_count}
score1 총합 :{total_score1}, 평균 : {average_chunk1:3f}
score2 총합 :{total_score2}, 평균 : {average_chunk2:3f}""")
print(f'전체 한 번에 처리 시간 : {time_all:7}초')
print(f"청크로 처리한 총 시간 : {time_chunk_total:7}초")

# 청크 처리 시간 시각화
# pip install koreanize-matplotlib - 터미널에서 설치
import matplotlib.pyplot as plt
import koreanize_matplotlib

labels = ['전체 한번에 처리', '청크로 처리']
times = [time_all, time_chunk_total]

plt.figure(figsize=(6,4))
bars = plt.bar(labels, times, color=['skyblue', 'red'])
for bar, time_val in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width() / 2, \
            bar.get_height(), f'{time_val:3f}초', \
            ha ='center', va='bottom', fontsize=10)

plt.ylabel('처리시간(초)')
plt.grid(linestyle ='--')
plt.tight_layout()
plt.show()


