class CoinIn:   # 동전을 넣는 사람 객체

    def __init__(self):
        self.coin = 0
        self.cupcount = 0
        self.cupPrice = 200

    def culc(self, coin, cupcount):
        self.coin = coin
        self.cupcount = cupcount
        change = self.coin - self.cupPrice * cupcount
        return change 

class Machine:

    def __init__(self):
        self.coin_in = CoinIn()

    def showData(self):

        total_coin = int(input("동전을 입력하세요 : "))
        total_cupcount = int(input("몇 잔을 원하세요 : "))

        total_change = self.coin_in.culc(total_coin, total_cupcount)

        if total_change >= 0:
            print(f"커피 {total_cupcount}잔과 잔돈 {total_change}원")

        else:
            print("요금이 부족합니다.")
            


if __name__ == "__main__":
    coffeemachine = Machine()
    coffeemachine.showData()







    
