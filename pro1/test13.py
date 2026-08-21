# 함수 장식자 : 기존의 함수 코드를 수정하지 않고도 함수의 앞뒤에 새로운 기능이나 추가작업을 더해주는 기법
# 함수 위에 장식자 이름을 붙여서 간단하게 사용할 수 있다.
# 새로운 기능 추가, 코드 중복 줄이기, 가독성 향상
# 기본 작동 원리 : 장식자는 함수를 인자로 받아 내부에서 새로운 함수를 감싸서 반환

def make2(fn):
    return lambda:"안녕" + fn()   #fn()함수를 실행하는것, 함수를 인자도 받으니 필요.

def make1(fn):
    return lambda:"반가워" +fn()

def helloFunc():
    return "홍길동"

hi = make2(make1(helloFunc)) #decorater 없이 실행
print(hi())

@make2   # helloFunc2()를 make1이 감싸고, 또 그 모든 것을 make2이 감싸는 형태
@make1
def helloFunc2():
    return "고길동"
print(helloFunc2())

print("-------------")
def traceFunc(func):   # 어떤 함수가 들어올건데, 그 함수를 func이라고 명명하자는 의미
    def wrapperFunc(a, b):
        r = func(a, b)
        print(f"함수명은 : {func.__name__} (a={a}, b ={b} -> {r})")
        return r
    return wrapperFunc # 함수 주소 반환

@traceFunc
def addFunc(a, b):
    return a + b

print(addFunc(10, 20))