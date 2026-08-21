# oop : 객체지향(중심)적인 프로그래밍 가능, 상속, 포함, 다형성 등의 기법 구사 가능
# class : 멤버 변수(필드), 멤버 메소드로 구성
# 인스턴스에 의해 새로운 이름공간을 갖는다.

import math

a = 2
print(a)

def func():
    print('ok')

class Testclass:   #클래스 이름은 대문자로 시작하는 것이 암묵적인 약속
    aa = 1 # 멤버 변수

    def __init__(self):  # method의 첫 인자는 반드시 self
        print("생성자")

    def __del__(self):
        print("소멸자")

    def showMessage(self):
        name = "한국인"
        print(name)
        print(self.aa)

test = Testclass()  #생성자를 호출, instance를 함. -> object(객체)이 생성됨
# Testclass(), 뒤에 괄호가 있으면 첫 번째 메소드가 실행됨

print("클래스 멤버 a :", test.aa)
test.showMessage()



