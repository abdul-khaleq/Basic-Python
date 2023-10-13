def call():
    print('calling someone I do not know')
    return 'call done'

class Phone:
    price = '23500'
    color = 'Black'
    brand = 'Redmi'
    features = ['camera', 'speaker', 'microphone']

    def call(self):
        print('calling one person')
    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text
myPhone = Phone()
print(myPhone.features)
myPhone.call()
result = myPhone.send_sms(513, 'I am ok')
print(result)