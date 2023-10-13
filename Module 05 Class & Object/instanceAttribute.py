class Shop:
    shopping_mall = 'Showpno'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # Cart is an instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)

ak = Shop('AK')
ak.add_to_cart('phone')
ak.add_to_cart('hradphone')
print(ak.cart)

ak2 = Shop('AK2')
ak2.add_to_cart('battary')
ak2.add_to_cart('charger')
print(ak2.cart)