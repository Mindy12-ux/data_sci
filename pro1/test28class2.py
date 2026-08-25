# 상속

class Person:   # 부모 클래스로 사용 
    say = "난 사람이야" # 접근권한이 public, 누구든지 접근 가능
    nai = "20"  # 클래스 내의 전역변수, 프로토타입
    __msg = "good : private 멤버, 현재 클래스에서만 유효하다"

    def __init__(self, nai):
        print("Person 생성자")
        self.nai = nai  # nai = init에서만 사용하는 지역변수, self.nai = 생성되는 객체에 저장되는 변수

    def printInfo(self):
        print(f'나이 : {self.nai}, 이야기 : {self.say}')

    def helloMethod(self):
        print("안녕")
        print("hello : ", self.say, self.nai, self.__msg)


print(Person.say, Person.nai)   # 원형 클래스로 멤버 호출, 비권장
# Person.printInfo()는 실행시키면 에러가 발생함

per = Person('25')

per.printInfo()
per.helloMethod()

print("--------------")

class Emploeyee(Person):
    subject = "근로자"
    say = "일하는 동물 ㅠㅠ"  # hiding(shadowing)
    #nai = 30

    def __init__(self):
        print("Employee 생성자")

    def printInfo(self):    # 메소드 오버라이딩(override)
        print("Employee 클래스의 printInfo 호출됨")
    

    def eprintInfo(self):
        print(self.subject, self.say, self.nai, sep = " / ")
        #print(self.__msg)  #부모 클래스의 메소드를 자식 '클래스'에서 호출했으므로 에러
        self.helloMethod()
        self.printInfo()  # 현재 클래스에서 먼저 검색 후 없으면 부모 메소드 호출
        super().printInfo() # 바로 부모 메소드 호출 (현재 클래스 검색 x)
        print(self.say, super().say)

    
emp = Emploeyee()
#emp.printInfo()
#print(emp.subject, emp.nai, emp.say)
print("------------")
emp.eprintInfo() # 부모 클래스에서 __msg를 호출했으므로 정상 작동
#per.helloMethod()

print("----------------------")

class Worker(Person):
    pass
    def __init__(self, nai):
        print("워커 생성자")
        super().__init__(nai) # 부모 클래스의 생성자 호출, Person 생성자로 결과가 출력됨


    def wPrintInfo(self):
        print("Worker - wPrintInfo() 처리")
        self.printInfo()
        super().printInfo()



wor = Worker("45")
print(wor.say, wor.nai, per.nai)
print("----------")
wor.wPrintInfo()

print("---------------")
class Programmer(Worker):
    def __init__(self, nai):
        print("프로그래머 생성자")
        #super().__init__(nai)  # 부모 생성자 호출, Bound method call
        Worker.__init__(self,nai)  # 위와 동일, UnBound method call
        #자식이 생성자를 가지고 있지 않으면 자동으로 부모의 생성자를 출력,
        #여기서는 부모의 생성자를 출력하고 싶어서 해당 코드 작성

    def pPrintInfo(self):
        print("프로그래머 클래스의 - pPrintInfo 처리함")

    #def wPrintInfo(self):
    #   print("프로그래머 클래스에서 오버라이딩")


pro = Programmer(70)
print("--------------")
#print(pro.say, pro.nai)
pro.pPrintInfo()
pro.wPrintInfo()  # 메소드 오버라이딩에 의해서 어떨때는 부모, 어떨때는 자식 클래스의 메소드들 출력함, 다형성 


print("\n클래스 타입 확인---------------")

a = 3 ; print(type(a))  # lass 'int'> made by Maker

print(type(pro))  # <class '__main__.Programmer'>
print(type(wor))    # <class '__main__.Worker'>

print(Person.__base__)       # <class 'object'> 모든 클래스의 슈퍼 클래스는 "object"
print(Emploeyee.__base__)    # <class '__main__.Person'>
print(Worker.__base__)       # <class '__main__.Person'>
print(Programmer.__base__)   # <class '__main__.Worker'>