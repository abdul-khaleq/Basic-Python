# Base class or Parent class or common attribute + functionality class
# Derived class or Child class or uncommon attribute + functionality
class Device:
    def __init__(self, brand, price, color, origin)->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.orgin = origin

    def run(self):
        return f'Running Laptop: {self.brand}'

class Laptop:
    def __init__(self, memory, ssd) ->None:
        self.memory = memory
        self.ssd = ssd


    def coding(self):
        return f'Learning and practicing python'

class Phone(Device):
    def __init__(self, brand, price, color, origin, dual_sim)->None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    def __repr__(self)->str:
        return f'Phone: {self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self, pixel)->None:
        self.pixel = pixel

    def change_lens(self):
        pass

my_phone = Phone('Redmi', 22500, 'silver', 'china', True)
my_phone.brand
print(my_phone)
