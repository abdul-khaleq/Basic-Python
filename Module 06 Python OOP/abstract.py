from abc import ABC, abstractmethod
# abstrat base class 
class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method
    def eat(self):
        print(f'I need food')
    @abstractmethod
    def move(self):
        print(f'I am coming')
class Monekey(Animal):
    def __init__(self, name)->None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print(f'Please give me banana')
    def move(self):
        print(f'Eated')

monkey1 = Monekey('monkey1')
monkey1.eat()
monkey1.move()