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

print('\npython, numpy, pytorch 간 형변환 가능')
print(7)
print(torch.tensor(7))                  # tensor(7)  상수 -> 텐서(스칼라)
print(torch.tensor(7).item())           # 7          텐서(스칼라) -> 상수
print(torch.tensor([1, 2]).numpy())     # [1 2]      텐서 -> numpy

arr = np.array([1, 2])
torch_arr = torch.tensor(arr)
print(torch_arr)                # tensor([1, 2])
print(torch.from_numpy(arr))    # tensor([1, 2])

print('사칙 연산 가능')
# torch.add()  .subtract()  .multiply()  .divide()
torch_result = torch.add(torch_arr, 5)
print(torch_result)

np_result = np.add(torch_result.numpy(), 2)
print(np_result)

print()
v1 = torch.tensor(1.0)
print('변경 전 v1 : ', v1, id(v1))      # 변경 전 v1 :  tensor(1.) 1337397605584
v1.fill_(100)                          # '치환', 새로운 객체를 가리키게 되는 것이 아니라, 기존 값을 갱신함, copy_(), add_(), sub_(), mul_(), div_()
print('변경 후 v1 : ', v1, id(v1))      # 변경 후 v1 :  tensor(100.) 1337397605584
v1 = 100                               # 새로운 객체를 참조 
print('변경 후 v1 : ', v1, id(v1))      # 변경 후 v1 :  100 140705837674712, 새로운 객체의 주소를 기억하게 됨.
# a = 5, 5의 주소를 가리킴
# a = 6, 6의 주소를 가리킴

print()
v1 = torch.tensor(1.0)
print(v1.data_ptr())            # 실제 data 저장 위치 출력, 5943328836928
v1.copy_(torch.tensor(123.0))
print(v1.data_ptr())            # 5943328836928
print('v1 : ', v1)

v2 = torch.ones((2, ))
print('v2 : ', v2)
print(v2.data_ptr())
v2.copy_(torch.tensor([30.0, 40.0]))    
print('v2 : ', v2)
print(v2.data_ptr())    # copy_()로 치환하면 같은 기억장소를 사용한다. '='로 치환하는 것과 다름.

print()
aa = torch.zeros((2, 1))
print('aa : ', aa)
aa.copy_(torch.ones((2, 1)))
print('aa : ', aa)
aa.add_(torch.tensor([[2.0], [3.0]]))
print('aa : ', aa)

print('난수 처리 ---- ')
torch.manual_seed(42)       # 고정 난수 재현
print(torch.rand(1))

# 균등 분포
print(torch.empty(2).uniform_(0, 1))
print(torch.empty(30000).uniform_(0, 1).mean())

# 정규 분포
print(torch.normal(mean=0.0, std=1.0, size=[3]))
print(torch.normal(mean=0.0, std=1.0, size=[30000]).mean()) 

print()
# GPU 텐서와 numpy 배열에서 알아둘 점
# PyTorch GPU 텐서는 GPU 연산과 자동 미분을 지원하지만, numpy 배열은 CPU 연산만 지원하므로 장치 간 변환과 메모리 공유 동작에 주의
if torch.cuda.is_available():
    gpu_tensor = torch.tensor([1,2,3], device='cuda')   # GPU에서 텐서 생성
    np_from_gpu = gpu_tensor.cpu().numpy()  # GPU 텐서를 cpu로 이동시킨 후 numpy 배열로 변환
    print(f'gpu 텐서 -> 넘파이 배열로 변환 : {np_from_gpu}')
else:
    print('cuda를 지원하지 않음')









