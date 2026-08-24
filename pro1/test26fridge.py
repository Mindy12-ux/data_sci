# 냉장고 객체에 음식 개체 저장하기

class FoodData:  # 냉장고에 보관될 객체(클래스)


    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date


class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print("냉장고 문이 열림")

    def close(self):
        self.isOpened = False
        print("냉장고 문이 닫힘")

    def foodList(self):   # 냉장고 문이 열린 경우 음식물 확인 메소드
        for f in self.foods:
            print(f" -{f.name} {f.expiry_date}")
        print()

    def put(self, thing):
        if self.isOpened == True:
            self.foods.append(thing)
            print(f"냉장고에 {thing.name} 넣음")

        else:
            print("냉장고 문이 닫혀있음")
  

fObj = Fridge()  # 냉장고 객체 하나 생성

apple = FoodData("사과", "2026-09-06")

fObj.open()
fObj.put(apple)   # 다른 클래스에 집어넣음, 이같은 경우도 클래스이 포함관계에 해당
fObj.close()

coke = FoodData("콜라", "2027-01-19")
fObj.open()
fObj.put(coke)
fObj.foodList()
fObj.close()


