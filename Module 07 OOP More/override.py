class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def  eat(self):
        print('rice, beaf, briyani')
    
    def exercise(self):
        raise NotImplementedError
    
class Cricketer(Person):
    def __init__(self, name, age, height, weight, term) -> None:
        self.term = term
        super().__init__(name, age, height, weight)
        
    # override
    def eat(self):
        print('vegetables')
    
    def exercise(self):
        print('gym')
    # + sign operator overload
    def __add__(self, other):
        return self.age + self.age
    # * sign overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height

    def __gt__(self, other):
        return self.age > other.age

sakib = Cricketer('Shakib', 38, 68, 91, 'BD')
rakib = Cricketer('Rakib', 38, 58, 81, 'BD')
# sakib.eat()
# sakib.exercise()

# overload
print(45 + 63)
print('sakib' + 'rakib')
print([1,5,6]+[3,5,7])
print(sakib + rakib)
print(sakib * rakib)
print(len(sakib))
print(sakib > rakib)