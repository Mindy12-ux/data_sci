class Animal:

    def move(self):
        pass


class Dog(Animal):
    name = "강아지"

    def move(self):
        return f"{self.name}꼬리 살랑살랑"



class Cat(Animal):
    name = "고양이"

    def move(self):
        return f"{self.name} 방울 짤랑짤랑"


class Wolf(Dog, Cat):

    pass


class Fox(Cat, Dog):

    def move(self, name):
        self.name = name
        return super().move()

    def foxMethod(self):
        return f"{super().name}와의 차이점은?"

# ani = Animal()

if __name__ == "__main__":

    dog = Dog()
    cat = Cat()
    wolf = Wolf()
    fox = Fox()

    print(dog.move())
    print(cat.move())
    print(wolf.move())
    print(fox.move("삐삐"))
    print(fox.foxMethod())