# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함관계 사용, 자원의 재활용
# 포함관계 : 다른 클래스(객체)를 마치 자신의 멤버처럼 선언하고 사용

#import test25handle
#test25handle.Handle.quantity

from test25handle import Handle

class Car:
    turnShowemessage = "정지"
    sum_quantity = 0
    def __init__(self, ownername):
        self.ownername = ownername
        self.handle = Handle()  # 클래스의 포함 관계


    def turnHandle(self, q):
        # 회전량 q : 양수면 우회전, 음수면 좌회전, 0이면 직진
        
        if q > 0:
            self.turnShowemessage = self.handle.rigthTurn(q)
            self.sum_quantity += q

        elif q < 0:
            self.turnShowemessage = self.handle.leftTurn(q)
            self.sum_quantity -= q

        elif q == 0:
            self.turnShowemessage = "직진"



if __name__ == "__main__":
    tom = Car("미스터 톰")
    tom.turnHandle(30)
    print(tom.ownername + "의 회전량은 " + tom.turnShowemessage + " " + \
    str(tom.handle.quantity))

    suji = Car("미스 수지")
    suji.turnHandle(-20)
    print(suji.ownername + "의 회전량은 " + suji.turnShowemessage + " " + \
    str(suji.handle.quantity))

    suji = Car("미스 수지")
    suji.turnHandle(0)
    print(suji.ownername + "의 회전량은 " + suji.turnShowemessage + " " + \
    str(suji.handle.quantity))
    print(id(tom))
    print(id(tom.handle))
    print(id(suji.handle))