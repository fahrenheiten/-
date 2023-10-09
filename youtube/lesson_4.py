import csv
class Item:
    pay_price = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity:0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate_price(self):
        return self.price*self.quantity
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return False
        else:
            return True

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    def apply_discount(self):
        self.price = self.price*self.pay_price

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity: 0,broken_phones=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
        Phone.all.append(self)
phone1=Phone("jscPhonev10",10,5,1)
print(phone1.calculate_price())
phone2=Phone("jscPhonev20",70,6,1)
