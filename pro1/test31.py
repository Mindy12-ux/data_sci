# 클래스의 다중 상속 - 부모 클래스가 복수 (순서에 유의)

class Tiger:
    data = "호랑이 세상"

    def cry(self):
        print("호랑이 : 어흥")

    def eat(self):
        print("맹수는 고기를 좋아해")
        print("아침에 닭고기, 낮에 소고기, 저녁에 돼지고기")



class Lion:
    data = "사자 세상"

    def cry(self):
            print("사자 : 으르렁")

    def hobby(self):
        print("백수의 왕은 낮잠이 취미")


class Liger1(Tiger, Lion):  # 두 개의 클래스를 상속받음
    pass

a1= Liger1()
a1.cry()    # 동일 멤버인 경우 첫 번째 클래스의 멤버를 출력한다
a1.hobby()
a1.eat()
print(a1.data)

print("--------------------")

def hobby():
    print("모듈의 멤버 일반함수")


class Liger2(Lion, Tiger):
    data = "라이거 만세"

    def Play(self):
        print("라이거 고유 메소드 - Play")

    def hobby(self):
        print("라이거는 공원 산책을 좋아해 - 오버라이딩")

    def showData(self):
        self.hobby()      # 1차적으로 현재 클래스에서 먼저 호출하고, 없으면 부모 클래스에서 호출
        super().hobby()   # 처음부터 부모 클래스에서 호출
        hobby()           # 클래스 바깥 : 모듈에서 함수 호출

        self.eat()        # Liger2 클래스에는 없으므로, 부모 클래스에서 호출함
        print(f"date : {self.data}, {super().data}")

a2 = Liger2()
print(a2.data)
a2.hobby()
a2.cry()
print("-----------")
a2.showData()

