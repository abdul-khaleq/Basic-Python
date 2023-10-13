from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from users import Customer, Employee, Manager,  Chef, Server
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Beaf Pizza', 600, 'large', ['beaf', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Chicken  Pizza', 400, 'large', ['chicken', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Potato  Pizza', 500, 'large', ['potato', 'water'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu 
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Burger', 1200, 'beef', ['cow', 'chili'])
    menu.add_menu_item('burger', burger_2)

    # add Drinks to the menu 
    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha coffee', 300, True)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()

    restaurant = Restaurant('Bangla Food', 2000, menu)
    # add employees 
    manager = Manager('kalaChan Manager', 123, 'kala@chan.com', 'kalipur', 1500, 'Jan 2020', 'core')
    restaurant.add_employee('manager', manager)
    chef = Chef('Rustom Babuchi', 1234, 'rustom@gmailcom', 'rustomNager', 3500, 'Feb 1, 2020', 'chef', 'everything')
    restaurant.add_employee('chef', chef)
    server = Server('chutu server', 1235, 'chutu@gmail.com', 'Sherpur', 200, 'March 1, 2020', 'server')
    restaurant.add_employee('server', server)
    # show employee 
    restaurant.show_employee()

    # customer 1 placing an order
    customer_1 =Customer('Shakib Khan', 123456, 'king@khan.com', 'banani', 100000)
    order_1 = Order(customer_1, [pizza_1,pizza_3, burger_1, burger_2, pizza_1, coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer one paying for order 1 
    restaurant.receive_payment(order_1, 20000, customer_1)
    print(restaurant.revenue, restaurant.balance)

    # customer 1 placing an order
    customer_2 =Customer('Shakib Chan', 12767, 'king@chan.com', 'Bashundhara', 50000)
    order_2 = Order(customer_2, [pizza_1, burger_2 , coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

     # customer one paying for order 2
    restaurant.receive_payment(order_2, 15000, customer_2)
    print('Revenue and balance after 2nd customer',restaurant.revenue, restaurant.balance)

    # pay rent 
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent ',restaurant.revenue, restaurant.balance, restaurant.expense)

    restaurant.pay_salary(chef)
    print('after salary ',restaurant.revenue, restaurant.balance, restaurant.expense)

if __name__ == '__main__':
    main()