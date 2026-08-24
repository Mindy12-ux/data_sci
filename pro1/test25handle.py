# 핸들 클래스 작성, 자동차나 자전거에 사용되어야지만 비로소 의미가 있는 클래스

class Handle:
    quantity = 0  # 핸들의 회전량
    #sum_quantity = 0

    def leftTurn(self,quantity):
        self.quantity = quantity
        #self.sum_quantity -= quantity

        return "좌회전"

    def rigthTurn(self,quantity):
        self.quantity = quantity
        #self.sum_quantity += quantity
    
        return "우회전"


# 첫 줄의 quantity와 self.quantity는 엄연히 다른 객체임
    
