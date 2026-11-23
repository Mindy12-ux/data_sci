# 딥러닝 모델 학습의 기본은 
# - 입력 데이터를 모델에 전달해 예측 결과를 얻고 
# - 지속적으로 그 결과와 실제값 간에 오차를 줄이기 위한 
# 모델의 파라미터(w, b)를 갱신하는 과정이다.

# 1) 직접 수식으로 구현

# 택시요금 예측 모델 : y = 2x + 5, 기본요금 5000원 + 거리당 2000 증가
def taxi_fare_model(distance):
    weight = 2  # 1km당 2천원
    bias = 5    # 기본요금 5천원
    fare = weight * distance + bias

    return fare

distance = 5    # 이동거리 5km
predicted_fare = taxi_fare_model(distance=distance)
print(f'{distance}km 이동 시 예상 택시요금 : {predicted_fare},000원')

print('--------------------')
# '실제 택시 요금은 13,000원이었다'라고 했을 때, 모델 예측값과 2000원 차이가 난다.
# 모델 오차 보정이 필요함. 가중치 수정이 필요.

actual_fare = 13
predicted_fare = 15
cost_error = predicted_fare - actual_fare
print(f'오차 : {cost_error}천원(너무 비싸게 예측)')

# 파라미터와 편향 수정 : 역전파
print('역전파 작업 : 파라미터 갱신(가중치와 편향)')
# 기존 모델 파라미터 
weight = 2; bias = 5; distance = 5
learning_rate = 0.01

