class Product:
    def __init__(self,name, id, weight):
        self.name=name
        self.id=id
        self.weight=weight

class Shop:
    def __init__(self) -> None:
        pass
    products_list = []
    def add_product(self, name, id, weight):
        product = Product(name, id, weight)
        self.products_list.append(product)

    def buy_product(self, product):
        for product in products_list.items():
            pass
            
        # if product in self.products:
        #     print(f"Congress! {product} is available")
        # else:
        #     print(f"{product} is not available")

potato = Shop()
potato.add_product("potato", 12,1)
potato.buy_product('potato')





