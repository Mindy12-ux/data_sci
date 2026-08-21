# 사용자 정의 함수
'''
def 함수명 (가인수):   # dummy argument, 매개변수
    # ...
    return 반환값   # 1개만 반환, return이 없으면 return None

함수명(실인수)  # 함수 호출
'''

print("뭔가를 실행...")
#함수 선언
def doFunc1():
    print("doFunc1 수행")


def doFunc2(name):
    print("name : ", name)

def doFunc3(arg1, arg2):
    res = arg1 + arg2
    return res

def doFunc4(a1, a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return      # 함수 내에 return은 함수의 무조건 탈출
    else:
        return imsi



# 함수 호출
doFunc1()
print("어떤 작업 처리")
doFunc1()
print("함수 주소는 ", doFunc1) # <function doFunc1 at 0x00000175BDA3F7F0> 16진수 주소가 찍힘
print("함수 주소는 ", id(doFunc1)) # 1605204441072 10진수로 표현된 주소임
imsi = doFunc1 # 함수의 "주소"를 치환한 것
imsi() # 함수를 실행할 수 있음
imsi2 = doFunc1() # 함수 실행 결과를 받은 것
print(imsi) # 실행 결과를 출력, <function doFunc1 at 0x000001FF2C01F8A0> 
print(id(doFunc1()))
print("----------")
print(doFunc2("jake"))
print(imsi)

print("---------")
doFunc3(3,5)
print(doFunc3("대한","민국"))
print(doFunc3(6,4))
print(doFunc3("3","4"))
result = doFunc3("3","4")
print("result : ", result)

print("---------")
print(doFunc4(2,4))
print(doFunc4(2,9))

print("---------")

def triArea(a, b):
    c = a * b / 2
    triAreaPrint(c) # 함수 내에서 다른 함수 호출


def triAreaPrint(arg):
    print("삼각형의 면적은 ", arg)

triArea(20, 30)

print("----------")

def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20,10):
    print("합격")
else:
    print("불합격")

print()
def swapFunc(a, b):
    return b, a  #튜플은 소괄호를 뺄 수 있음, return (a, b)와 같은 의미, return [a, b], return {a, b} 모두 가능
# 함수의 반환값은 무조건 하나임

a = 1; b = 20
print(a, " ", b)
print(swapFunc(a,b)) # (20, 1) '하나'의 집합을 return

print()

def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print("내부함수 funcInner 실행")

    funcInner()  # inner함수는 test 함수 안에서만 호출이 가능함 

funcTest()

print()
# if 조건식 안에 함수 적용

def isOdd(para):
    return para % 2 == 1 # 홀수이면 True 반환

mydict = {x : x for x in range(11) if isOdd(x)}  # 홀수이면 출력 
print(mydict)



print("\n변수의 생존 범위 (scope rule)")
# 변수가 저장되는 이름공간은 변수가 어디에서 선언되었는가에 따라 생존 시간이 다르다.
# 전역, 지역 변수
# Local > Enclosing funtion > Global > Built-in
player = '전국대표'  #전역변수 (현재 파일(모듈) 어디서든 호출 가능)
name = "신기해"

def funcSoccer():
    name = "이기자"   #지역변수 (현재 함수 내에서만 유효)
    city = "서울"
    print(f"이름은 {name} 수준은 {player}")
    print(f"지역은 {city}")

funcSoccer()
print(f"이름은 {name} 수준은 {player}")


print()

a = 10; b = 20; c = 30
print(f"bar 수행 전 a:{a}, b:{b}, c:{c}")

def foo():
    a = 7 #지역 변수
    b = 100

    def bar():
        global c # bar의 멤버가 아니라 모듈의 멤버가 됨 (전역)
        nonlocal b # bar의 멤버가 아니라 , bar의 상위 수준의 함수 foo의 지역 변수가 됨
        b = 8 #지역 변수
        print(f"bar 수행 중 a:{a}, b:{b}, c:{c}")
        c = 9
        b = 200  #bar 수준의 지역 변수

    bar()
    print(f"bar 수행 후 a:{a}, b:{b}, c:{c}")

foo()
print(f"foo 수행 후 a:{a}, b:{b}, c:{c}")

print()

g = 1
print("g :", g)
def func():
    global g
    a = g
    g = 2 # 이것 때문에 g가 지역변수가 되어버림.
    return a
print(func())
print("g : ", g)



