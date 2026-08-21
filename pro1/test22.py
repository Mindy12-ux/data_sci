kor = 100 # 모듈의 멤버 : 전역변수

def abc():
    kor = 0 # 함수 내의 지역변수

    print("모듈의 멤버 함수")


class My:
    kor = 80 # my 클래스 멤버 변수

    # def __init__(self):    # 생성자 호출 - 초기화 작업이 없는 경우 생성자는 생략 가능
    #     pass

    def abc(self):
        print("My 클래스 멤버 메소드")

    def show(self):
        #kor = 77 # 메소드 내의 지역변수
        print(kor)  # kor = 77이 들어있는 경우 77, 없는 경우 모듈의 멤버(100)를 출력함
        print(self.kor)   # 80

myObj = My()
myObj.show()
print()
myObj2 = My()
print(myObj2.kor)
myObj2.kor = 99
print(myObj2.kor)

print("~"*30)
myObj3 = My()
print(myObj3.kor)



