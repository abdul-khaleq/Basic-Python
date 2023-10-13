class Product:
    def __init__(self, product):
        self.product = product

class Shop:
    products = []
    def add_product(self, item):
        product = Product(item)
        self.products.append(product.product)

    def buy_product(self, product):
        if product in self.products:
            print(f"Congress! {product} is available")
        else:
            print(f"{product} is not available")

potato = Shop()
potato.add_product("potato")
potato.add_product("mula")
# potato.add_product("vendi")
potato.buy_product('potato')
potato.buy_product('mula')
potato.buy_product('vendi')




