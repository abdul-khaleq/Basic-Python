class E_Shopping:
    users = []
    products = []
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        E_Shopping.users.append(self)

class Customer(E_Shopping):
    def __init__(self, name, email, password, type):
        super().__init__(name, email, password)
        self.type = type

    def show_product(self):
        for product in self.products:
            print(f'Product name: {product.productName} with Price: {product.productPrice} and Weight: {product.productWeight}')
        
class Product:
    def __init__(self, productName, productPrice, productWeight):
        self.productName = productName
        self.productPrice = productPrice
        self.productWeight = productWeight
       
    
class Seller(E_Shopping):
    def __init__(self, name, email, password, type):
        super().__init__(name, email, password)
        self.type = type

    def add_product(self, productName, productPrice, productWeight):
        product = Product(productName, productPrice, productWeight)
        self.products.append(product)


seller = Seller('ABdul Khaleq', 'abdulkhaleq6008@gmail.com', 132, 'male')
print(seller.users[0].name)
seller.add_product('Potato', 38, 1)
seller.add_product('Rice', 58, 1)
seller.add_product('Chili', 68, 1)
print(seller.products[0].productName)

customer = Customer('ABdul Khaleq', 'abdulkhaleq6008@gmail.com', 132, 'male')
customer.show_product()


print('1. Option 1 to SignIn as a custome')
print('2. Option 2 to SignUp as a seller')
option = int(input('Enter option: '))
if option == 1:
    name = input('Your name: ')
    email = input('Your email: ')
    password = input('Your password: ')
    Customer(name, email, password, type)