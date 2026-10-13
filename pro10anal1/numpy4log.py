# 편차가 큰 데이터에 대한 로그 변환
# 큰 값을 압축해서 데이터 간 격차를 줄이는 변환이 가능

# ML에서 데이터 분석 시 log를 사용하면?
# 1) 스케일 차이를 축소해준다
# 2) 로그변환하면 치우친 데이터를 정규분포에 가깝게 변경해준다
# 3) 모델링에서 지수관계를 선형 관계로 바꿔준다.

import numpy as np
np.set_printoptions(suppress=True, precision=6) # 과학적 표기형식 해제, 모두 숫자로 보일 수 있게 함

def test():
    values = np.array([345, 34.5, 3.45, 0.345, 0.01, 0.1, 10, 100])
    print(np.log2(3.45), ' ', np.log10(3.45), ' ', np.log(3.45))

    print("원본값 : ", values)
    log_values = np.log10(values)
    print('log_values : ',log_values)   # 상용로그

    ln_values = np.log(values)
    print('ln_values : ',ln_values)     # 자연로그 : ML(Machine Learning)에서 주로 사용

    # 데이터 분석과 머신러닝에서 정규화(Nomalization/Min-Max Scaling)와 표준화(Standardization)는 서로 다른 스케일을 가진 특성(Features)들을 일정한 기준으로 맞춰주는 피처 스케일링 방법이다.
    
    # 정규화 : 모든 데이터를 0 ~ 1 사이 범위 내에 출력, 정규화/표준화 실행 여부에 따라 모델 성능의 편차가 심해짐
    # 정규화 계산식 : (데이터 - 최솟값) / (최대값 - 최소값)
    min_val = np.min(values)
    max_val = np.max(values)
    normalized = (values - min_val) / (max_val)
    print('정규화 결과 : ', normalized)

    # 표준화 : 데이터의 평균을 0, 표준편차를 1이 되로록 변환하는 방식
    # 표준화 계산식 : (데이터 - 평균) / 표준편차
    mymean = np.mean(values)
    mystd = np.std(values)
    standardized = (values - mymean) / mystd
    print("\n표준화 결과 : ", standardized)

class LogTrans:
    # 편차가 큰 데이터를 로그 스케일 변환하고 그 역벽환을 제공하는 클래스
    def __init__(self, offset:float=1.0):   # offset : 보정값 (log(0) 피하기)
        self.offset = offset

    # 로그 변환 메소드
    def transform(self, x:np.ndarray) -> np.ndarray:
        return np.log(x + self.offset)

    # 역 변환 메소드
    def inverse_transform(self, x_log:np.ndarray) -> np.ndarray:
        return np.exp(x_log) - self.offset

test()

print('----------------')
data = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], dtype=float)
logObj = LogTrans()
data_log_scaled = logObj.transform(data)    # 로그 변환
reversed_data = logObj.inverse_transform(data_log_scaled)   # 역변환

print('원본 자료 : ', data)
print('로그 변환 : ', data_log_scaled)
print('역 변환 : ', reversed_data)

