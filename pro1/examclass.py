class CoinIn:   # 자판기에 돈을 넣는 사람 객체, coin, change, cupCount가 왜 있어야 하는지 모르겠음 
    coin = 0
    change = 0

    def culc(self, coin, cupCount):
        self.coin = coin
        self.cupCount = cupCount
        self.change = self.coin - 200 * cupCount
        return self.change


class Machine:
    def __init__(self):
        self.person = CoinIn()
    
    def showdData(self):
        total_coin = int(input("동전을 입력하세요 : "))
        total_cupCount = int(input("몇 잔을 원하세요 : "))

        total_count = self.person.culc(total_coin, total_cupCount)
        
        if total_count > 0 :
            print(f"커피 {total_cupCount}잔과 잔돈{total_count}원")
        
        else:
            print("요금이 부족합니다.")


if __name__ == "__main__":
    coffeemachine1 = Machine()
    coffeemachine1.showdData()







    
