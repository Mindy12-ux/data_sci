# 모듈은 파이썬 파일 하나에 정의된 함수, 클래스, 변수 등을 모아둔 것. 즉, 관련된 코드들을 하나의 파일로 정리한 것이 모듈임
# 패키지는 여러 모듈을 디렉토리 구조로 묶어 관리하는 것, 패키지로 인식되기 위해서는 __init__ 파일이 포함되어 있어야 함
# 모듈의 멤버로 모듈, 함수, 클래스, 변수, 실행문이 있다.
#하나의 파일은 하나의 모듈이 된다.

print(print.__module__)

print("뭔 작업을 하다가 ... 외부 모듈 사용하기")
import sys
print(sys.path)  # 현재 모듈의 경로를 볼 수 있음

q = "n"
if q == "y":
    sys.exit()  #프로그램 실행 중에 무조건 실행 종료 


# 수학관련 모듈 읽기
import math
print(math.exp(199))
print(math.sin(math.radians(30)))

# 달력 출력
import calendar
print(calendar.TUESDAY)
calendar.prmonth(2026,8)
del calendar

# import time
# print("3초 휴식")
# time.sleep(3)
# print("계속")

# 난수 출력
import random
print(random.random())
print(random.randrange(1, 10))

from random import random  #호출시에 모듈명을 쓰지 않아도 됨
print(random())

from random import randint, randrange, choice
print(randrange(1,100))
print(randint(1, 5))
print(choice("seios"))

from random import *   # 전체 모듈을 로딩 (비권장, 메모리를 너무 많이 차지함)


print("종료")

