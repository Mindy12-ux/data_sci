# 파이토치는 파이썬 기반의 오픈소스 딥러닝 및 머신러닝 프레임워크이다.
# 핵심 특징
# 동적 계산 그래프 : 코드 실행 시점에 동적 그래프를 생성한다. 디버깅과 모델 구조 실험이 직관적이다.
# 텐서 및 자동 미분 
# 성능 최적화 및 분산 학습
# 하드웨어 호환성

# 모듈 설치
# pip install torch torchvision torchaudio
# pip install tensorflow        참고용

# tensor와 numpy의 차이 : 형변환 -> tensor값 변경 -> in-place 연산 -> 난수 흐름

import torch
import numpy as np

print(torch.__version__)    # 2.15.0+cpu
print('GPU 사용 가능 여부 : ', torch.cuda.is_available())
print('GPU 장치 정보 : ', torch.cuda.get_device_name(0) if torch.cuda.is_available() else [])
# pyTorch는 기본적으로 Eager Execution(즉시 실행) 방식으로 동작

print('\nTensor : PyTorch에서 데이터를 담는 기본 자료구조 (숫자 데이터 저장용 다차원 배열)')
# ndarray와 유사하나 PyTorch 연산에 사용되도록 만들어진 객체 (딥러닝 연산, GPU연산, 자동 미분이 가능해짐)
print(12, type(12))                                     # 12 <class 'int'>, 파이썬 상수. 파이썬이 직접 관여하는 상수 
print(torch.tensor(12), type(torch.tensor(12)))         # tensor(12) <class 'torch.Tensor'>, 0d 텐서 (scaler)
print(torch.tensor([12]))                               # tensor([12]) 1d 텐서 (vector)
print(torch.tensor([[12]]))                             # tensor([[12]]) 2d 텐서 (matrix)
print(torch.tensor([[12, 1]]))                          # tensor([[12,  1]])

print('\nTensor 속성 확인 (텐서의 차원수 확인)')
print(torch.tensor([[12, 1]]).dim())        # 2
print(torch.tensor([[12, 1]]).ndim)
t = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)    
print('shape : ', t.shape)      # torch.Size([2, 3])
print('dtype : ', t.dtype)      # torch.float32    

print()
imsi = np.array([1, 2])
print(imsi, type(imsi))         # [1 2] <class 'numpy.ndarray'>
imsi[0] = 10
print(imsi)                     # [10  2]

# PyTorch Tensor
a = torch.Tensor([1, 2])
print(a, type(a))               # tensor([1., 2.]) <class 'torch.Tensor'>
a[0] = 10
print(a)                        # tensor([10.,  2.]), 텐서플로우에서는 안됨.

print()
a = torch.tensor([1, 2])
b = torch.tensor([3, 4])
c = a + b   # 텐서 요소 더하기
print(c)    # tensor([4, 6])
d = torch.tensor([3])   # 텐서도 브로드캐스트 연산 가능
e = c + d
print(e)    # tensor([7, 9])
