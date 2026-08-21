# 상품 주문 및 할인 처리 프로그램
#상품명과 수량을 전달받아 주문 금액을 계산하는 order()함수 작성
#할인 함수는 lambda를 이용하여 작성한다

products = {
    "노트북": 1500000,
    "모니터": 350000,
    "키보드": 80000,
    "마우스": 50000
}

def order(product, count, discount_func= 0 ):
    
    totPay = 0
    price = 0
    material = list(products.keys())

    for i in range(4):    
        if product == material[i]:
            
            totPay = lambda 



order("노트북",1)



###리스트에 있는 원소가 '몇 번째'에 있는지 확인할 수 있는 방법이 있나?



