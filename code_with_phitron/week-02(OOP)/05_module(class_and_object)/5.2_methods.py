def call():
    print("Calling someone I don't know")
    return "I call back"

class Phone:
    price = 1000
    color = 'Black'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print("Calling one person")

    def send_sms(self, phone, sms):
        text = f"Sending sme to: {phone} and message: {sms}"
        return text


my_phone = Phone()

print(my_phone.features)
my_phone.call()
result = my_phone.send_sms('01750659659', 'I forgot to miss you')
print(result)




