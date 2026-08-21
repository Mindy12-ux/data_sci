# closure : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
# 내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기

def funcTimes(a ,b):
    c = a * b
    print("c :", c)
    return c

print(funcTimes(2, 3), funcTimes)
# print("c :", c) c를 선언한 적이 없으므로 에러
# print(funcTimes)

# kbs = funcTimes(2, 3) #함수실행 결과를 치환한 것
# print(kbs)
# kbs = funcTimes  # 함수 주소를 치환한 것 (함수의 별명이 하나 생긴 것)
# print(kbs)
# print(kbs(2,3), id(kbs(2,3)))
# print(id(kbs), id(funcTimes))

# mbc = sbs = kbs
# del funcTimes  # funcTimes 함수명 삭제, 그렇지만 mbc 등이 함수가 저장되어 있는 주소를 기억하기 때문에 함수는 사용할 수 있음

print("\n---- 클로저를 사용하지 않은 경우 -----")
def out():
    count = 0 
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())

print(out(), out)

#print(count) #이건 에러
out()  # print()하지 않았으므로, out()의 return값 none이 찍히지 않는 것임.
# a= out()
# print(id(a),id(out))

print("\n---- 클로저를 사용한 경우 -----")

def outer():
    count = 0 
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # 요것이 클로저 : 내부 함수 내 객체의 '주소'를 반환

var1 = outer()
print("var1 주소 :", var1)
# var1 주소 : <function outer.<locals>.inner at 0x000001E8310A35E0>

print("count :", var1())  # count : 1
print("count :", var1())  # count : 2
# print(var1.count) 외부에서 직접 접근을 불가

print("클로저 내부 확인 : ",var1.__closure__)  # __명령__ : 파이썬 고유 명령
# 클로저 내부 확인 :  (<cell at 0x0000024C1ACEB6D0: int object at 0x00007FFACF35E498>,)
myvar = var1() #3
#myvar = var1 #<function outer.<locals>.inner at 0x0000020ACE343480>
print(myvar)
print()
var2 = outer() # 새로운 객체(inner 함수) 생성
print(var2())
print(var2())

print("\n수량 * 단가 * 세금한 결과를 출력하기 ---")
def outer2(tax):
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2

# 1분기에는 금액 : su * dan에 대한 tax는 0.1% 부과
q1 = outer2(0.1)
result1 = q1(5, 50000)
print("result1 : ",result1)
result2 = q1(2, 10000)
print("result2 : ",result2)

q2 = outer2(0.05)
result3 = q2(5, 60000)
print("result3 : ",result3)
result4 = q2(2, 10000)
print("result4 : ",result4)

print(id(q1), id(q2)) #1926892828304 1926892828480
print(id(var1), id(var2)) #2624535737824 2624535799312
# 같은 inner 함수를 참조하지만 객체가 저장된 주소는 다름

print("\n\n일급함수, 일급객체 : 함수를 변수나 상수에 저장, 함수 안의 함수, 인자로 함수 전달, 반환 값이 함수")
def func1(a , b):
    return a + b

func2 = func1  # 함수를 변수나 상수에 저장
print(func1(3,4))
print(func2(3,4))

print()
def func3(fu): # 인자로 함수 전달
    def func4():  # 함수 안에 함수 
        print("나는 내부 함수야")
    func4()
    return fu  # 반환 값이 함수

mbc = func3(func1) # 인자로 함수 전달함
print(mbc(6,7))

print("\n축약함수(Lamda function) : 여러 줄의 함수 정의를 한 줄로 줄여서 쓰는 익명 함수")
# lambda 매개변수, ... : 표현식  ==> return없이 결과 반환

def hapFunc(x , y):   #프로그램 종료시까지 메모리를 유지함
    return x + y
print(hapFunc(3,3))

# 람다로 표현

print((lambda x, y: x + y)(1, 2))  # 휘발성, 실행과 동시에 메모리 사라짐

gg = lambda x, y: x + y
print(gg)  # <function <lambda> at 0x0000025CB0293A00>
print(gg(4,5))

gg2 = lambda x, y: x + y
print(id(gg), id(gg2))
print((lambda x, y: x + y) is (lambda x, y: x + y)) #False
print(outer2 is outer2) #True

print()
kbs = lambda a, su =10: a + su
print(kbs(5))
print(kbs(5,6))

# print()
# sbs = lambda a, *tu, **di: print(a, tu, di)
# sbs(1,2, 3, var1=4, var2=5)  # 1 (2, 3) {'var1': 4, 'var2': 5}, sbs 자체로 함수
# print(sbs)  # function <lambda> at 0x000001BF6EAA3C10>

# print("\n임의의 함수에서 람다 사용하기")
# #filter() : # 반복 가능한 객체에서 특정 조건에 맞는 요소만 골라낼 때 사용한다
# # 기본 구조는 filter(함수, 반복가능한 객체)
# print(list(filter(lambda a: a< 5, range(10))))  #[0, 1, 2, 3, 4]
# print(list(filter(lambda a: a % 2, range(10)))) #[1, 3, 5, 7, 9], True만 출력하기 때문에 홀수만 찍힘
# #print(bool(0),bool(1)) # lse True

# # filter를 이용해 1 ~ 100 사이의 정수 중 5의 배수'이거나' 7의 배수만 출력(리스트로)

# print(list(filter(lambda a: a % 5 == 0 or a % 7 == 0, range(1, 101))))


