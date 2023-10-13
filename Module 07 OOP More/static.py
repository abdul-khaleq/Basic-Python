class Shopping:
    cart = [] # class attribute, static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = name # instance attribute
        self.location = location
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying: {item} for price: {price} and remaining: {remaining}')
    
    @staticmethod
    def multiply(a,b):
        result = a*b
        print(result)
    
    @classmethod
    def just_for_see(self, item):
        print('Just for seeing', item)

sherpur = Shopping('Sherpur Plaza', 'Sherpur')
# sherpur.purchase('Shirt', 1000, 5000)
sherpur.just_for_see('Sunglass')
# Shopping.purchase('OK','Shirt 2', 10000, 50000)

# static method 
Shopping.just_for_see('Glass')
Shopping.multiply(4,5)
    