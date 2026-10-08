# 배열 연산
# 기본 수학 함수는 배열에 요소별로 적용되고, 
# +, -, *, / 나 add, subtract, multiply, divide 함수를 사용한다.
# 벡터화 연산을 하므로 for문을 사용하지 않고 바로 배열에 대한 연산을 할 수 있다.

import numpy as np

# x = np.array([[1,2], [3,4]], dtype=np.float32)  # 데이터 타입을 float32로 지정 
x = np.array([[1.,2], [3,4]])   # float64, int보다 float의 데이터 타입이 높기 때문에 모든 데이터가 float이 됨
print(x, ' ', x.dtype)  

y = np.arange(5, 9)     # arange : python의 ragne와 같은 것, [5 6 7 8]   int64
y = np.arange(5, 9).reshape(2, 2)   # 구조 변경 (1차원 -> 2차원), [[5. 6.] [7. 8.]]
y = y.astype(np.float32)            # type 변경
print(y, ' ', y.dtype)              # [[5. 6.] [7. 8.]]
print(x.ndim,' ', y.ndim)           # 2, 2 둘 다 2차원

print()
print(x + y)        # 파이썬 연산자 사용
print(np.add(x, y)) # 넘파이 함수(유니버설 함수:내부적으로 벡터화 연산을 수행함, 그래서 빠름) 사용, 위 방법에 비해 연산속도가 빠르다 : [[ 6.  8.] [10. 12.]]
print()
print(x - y)       
print(np.subtract(x, y))
print()
print(x * y)   
print(np.multiply(x, y))
print()
print(x / y)        
print(np.divide(x, y))
print()
print(np.sqrt(x),'\n', np.exp(x),'\n', np.log(x),'\n', np.cos(x))