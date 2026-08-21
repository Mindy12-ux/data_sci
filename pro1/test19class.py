# oop : 객체지향(중심)적인 프로그래밍 가능, 상속, 포함, 다형성 등의 기법 구사 가능
# class : 멤버 변수(필드), 멤버 메소드로 구성
# 인스턴스에 의해 새로운 이름공간을 갖는다.

import math

a = 2
print(a)

def func():
    print('ok')

class Testclass:   #클래스 이름은 대문자로 시작하는 것이 암묵적인 약속

    aa = 1 # 멤버 변수, 현재 클래스 내에서 전역

    def __init__(self):  # 특별 메소드, Method의 첫 인자는 반드시 self
        print("생성자: 객체 생성시 가장 먼저 1회만 호출, 초기화를 담당")

    def __del__(self):   # 특별 메소드
        print("소멸자 : 프로그램 종료 시 자동실행, 마무리 작업")

    def showMessage(self):  # 일반 메소드
        name = "한국인"    # 지역변수 : showmessage에서만 유효
        print(name)
        print(self.aa)  #그냥 aa만 찍으면 showmessage내에서 찾음, 클래스 내 변수를
        #찾고싶으면 앞에 self를 붙어야 함.

test = Testclass()  #생성자를 호출, instance를 함. -> object(객체)이 생성됨
# Testclass(), 뒤에 괄호가 있으면 첫 번째 메소드가 실행됨
# 변수 = 클래스이름() :  클래스를 호출하는게 아니라 생성자를 호출하는 것
# test = Testclass(test)와 같은 의미

print("클래스 멤버 a :", Testclass.aa) # 클래스 멤버 a : 1
print("클래스 멤버 a :", test.aa)   # 클래스 멤버 a : 1

#Testclass.showMessage()  에러 발생
test.showMessage() #여기선 에러가 발생하지 않음
# test = showmessage(test)와 같은 의미, 클래스 생성자를 \
# 이용해 객체 생성 후 해당 개체의 주소를 객체변수에 치환

print()
print(Testclass)  # <class '__main__.Testclass'>
#argument self의 유무로 메소드와 함수를 구분함, self가 있으면 클래스 내 메소드

print()
# test = class()를 주면, class속성을 가진 test라는 객체가 만들어짐
# 함수 클로저 예시와 비슷

# 2. Unbound method call
Testclass.showMessage(test)  #Testclass.showMessage()  에러 발생


# 1. Bound method call
test.showMessage() #여기선 에러가 발생하지 않음, # test = showmessage(test)와 같은 의미, 클래스 생성자를 \
# 이용해 객체 생성 후 해당 개체의 주소를 객체변수에 치환

print(test.__dict__)

print()

print(type(1))  # <class 'int'>
print(type(1.0))
print(type("ok"))
print(type(test))   # <class '__main__.Testclass'> Testclass 타입, 새로운 타입을 만드는 것


print(id(test))  # 2330848415424
print(id(Testclass))  # 2330850572128
test2 = Testclass()  # 객체 한 개 더 생성
print(id(test2))  # 2330848333328



