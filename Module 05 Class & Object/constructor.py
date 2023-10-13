class Phone:
    manufactured = 'China'
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    def send_sms(self, phone, sms):
        text = f'sending to: {phone} and message: {sms}'
        print(text)

myPhone = Phone('AK', 'Redmi', 22500)
print(myPhone.owner, myPhone.brand, myPhone.price)

herPhone = Phone('Jenny', 'iPhone', 120000)
print(herPhone.owner, herPhone.brand, herPhone.price)