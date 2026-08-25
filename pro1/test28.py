# 상속 : 자원의 재활용을 목적으로 특정 클래스의 멤버를 가져다 쓰는 것
# 코드 재사용
# 확장성 - 기존 클래스에 새 기능을 추가한 새로운 클래스 생성
# 구조적 설계 - 공통개념은 부모 클래스, 구체적 내요을 자식 클래스에서 구현
# 다형성 구사 - 메소드 오버라이딩

class Animal:
    age = 1

    def __init__(self):
        print("Animal 생성자")


    def move(self):
        print("움직이는 생물")


class Dog(Animal):

    def __init__(self):
        print("Dog 생성자")

    def my(self):
        print("댕댕이라고 해요~~~")

# 상속 - Animal : 부모, 조상, super, parents, 상위 클래스
# 상속 - Dog : 자식, 자손, sub, child, 파생, 하위 클래스

dog1 = Dog()   # 다른 언어와는 다르게 시행시 부모 생성자는 실행하지 않고 자식 생성자만 실행함
dog1.my()
dog1.move()
print("dog1 age : ",dog1.age)
print()
dog2 = Dog()
dog2.my()
print("dog2 age : ",dog2.age)
dog2.move()


class Horse(Animal):
    pass

print("------------------")
horse1 = Horse()  # 자식의 생성자가 없을 경우 부모 생성자 호출
print(horse1.age)
horse1.move()