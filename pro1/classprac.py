"""     편의점에서 상품을 구매하고 결제하는 프로그램을 작성하세요.

클래스는 다음과 같이 구성합니다.

ConvenienceStore
 └── Payment

ConvenienceStore 클래스
storeName : 편의점 이름
payment : Payment 객체를 포함관계로 가짐

Payment 클래스
money : 현재 투입한 금액
change : 거스름돈      """

class Payment:

    def __init__(self): 
        self.money = 0
        self.change = 0

    def moneyInput(self, money):
        self.money = money
        self.change = money - 2500
        return self.change

class ConvenienceStore:

    def __init__(self, storename):
        self.payment = Payment()
        self.Storename = storename

    def calculate(self):
    
        total_pay = int(input("돈을 넣으세요 : "))
        changes = self.payment.moneyInput(total_pay)

        if total_pay >= 2500:
            print(f"{self.Storename}, 결제 완료 \n거스름돈은 {changes}원 입니다.")

        else:
            print("금액이 부족합니다.")


if __name__ == "__main__":
    my_conv = ConvenienceStore("안국점")
    my_conv.calculate()


