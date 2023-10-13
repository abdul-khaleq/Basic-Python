class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def eat(self):
        print(self.name, "can eat")

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def speak(self):
        print("I can speak")

class Dog(Animal):
    def speak(self):
        print("I can say Hello")

c = Cat('Cat')
c.eat()
d =Dog("Dog")
d.eat()