class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)
    
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Tota price',total)
        if amount < total:
            print(f'Please provide {total -amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')

ak = Shopping('AK')
ak.add_to_cart('alu', 50, 6)
ak.add_to_cart('dim', 12, 24)
ak.add_to_cart('rice', 50, 5)

# print(ak.cart)
ak.checkout(1000)