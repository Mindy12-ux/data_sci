# function : 여러 개의 수행문을 하나의 이름으로 묶은 실행단위
# 함수 고유의 공간을 갖는다.
# 자원의 재활용이 가능하다

# 내장함수
print(sum([1,2,3]))
print(8, bin(8))
print(eval("4 + 5"))
print(round(1.2), round(1.62))
import math
print(math.ceil(1.223), "", math.ceil(1.6)) # 올림
print(math.floor(1.223), "", math.floor(1.6)) # 내림

b_list = [True, 1, False]
print(all(b_list)) # False, all : 모두 참이어야 True
print(any(b_list)) # True, any : 하나라도 참이면 True

data1 = [10,20,30]
data2 = ["a", "b"]
for i in zip(data1, data2):
    print(i)
# zip 많이 쓰게 될 것임, 두 데이터를 꺼내서 쌍을 이루어줌
# (10, 'a')
# (20, 'b')

import builtins # 자동 로딩
builtins.print("자동 로딩")

