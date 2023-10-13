class Restaurant:
    def __init__(self, restaurant_name) -> None:
        self.restaurant_name  = restaurant_name
        self.customers = []


class Customer:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def order(self, item):
        self.item = item
    
    def get_order(self):
        return f'order is ready. Here you are {self.item}'

