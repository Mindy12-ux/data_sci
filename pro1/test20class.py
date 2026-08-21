class Car:
    handle = 1
    speed = 0

    def __init__(self, name, speed):
        self.name = name # 현재 변수의 name에게 name(지역변수) 인자값 치환
        self.speed = speed 

    def showData(self):
        km = "킬로미터"
        msg = "속도 :" + str(self.speed) + km

        return msg

    def printHandle(self):
        return self.handle


print(Car.handle) # 원형(prototype) 클래스의 멤버 호출, 원형 클래스 'car'는 원형 클래스의 주소를 기억하고 있음
car1 = Car("morning", 50) # 생성자 호출을 통해 객체 생성(인스턴스화), 새롭게 생성된 객체의 주소를 기억하고 있음

print("car1 객체 주소 :", car1)
print("car1 :", car1.handle, car1.name, car1.speed, sep=", ")
# car1.handle 값이 객체별로 주어져있지 않다면 원형 클래스의 값을 찍어냄

car1.color = "파랑"  #원형 클래스에 없는 값도 추가할 수 있음
print("car1.color :",car1.color)

print("-"*30)
car2 = Car("oscar", 100)
print("car2 객체 주소 :", car1)
print("car2 :" , car2.handle, car2.name, car2.speed, sep=" ")

print(id(Car), id(car1), id(car2))
print(car1.__dict__)  # 각 객체의 멤버 확인 가능
print(car2.__dict__)

a= [i for i in car1.__dict__.values()]
print(a)

print("-"*15, "메소드", "-"*15)
print("car1 speed : ", car1.showData())
print("car2 speed : ", car2.showData())

car1.speed = 110
car2.speed = 40
print("car1 speed : ", car1.showData())
print("car2 speed : ", car2.showData())

print("car1 handle : ", car1.printHandle())

Car.handle = 2  # 원형 클래스의 값 수정
print("car1 handle : ", car1.printHandle())

