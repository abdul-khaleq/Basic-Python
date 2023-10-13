# poly --> many (multiple)
# morph --> shape

class Animal:
    def __init__(self, name)->None:
        self.name = name
    def make_sound(self):
        print(f'{self.name} is making sound')

class Cat(Animal):
    def __init__(self, name)->None:
        super().__init__(name)
    def make_sound(self):
        print(f'{self.name} meow meow')

class Dog(Animal):
    def __init__(self, name)->None:
        super().__init__(name)
    def make_sound(self):
        print(f'{self.name} gheu gheu')

class Goat(Animal):
    def __init__(self, name)->None:
        super().__init__(name)
    def make_sound(self):
        print(f'{self.name}meh meh')

cat = Cat('Cat')
cat.make_sound()

dog = Dog('Dog')
dog.make_sound()

goat = Goat('Goat ')
goat.make_sound()

animals = [cat,dog, goat]
for animal in animals:
    animal.make_sound()