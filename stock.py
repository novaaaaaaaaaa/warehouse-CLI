from typing import Any


class Stock:
    def __init__(self, stockid, name, description, price):
        self.stockid = int(stockid)
        self.name = name
        self.description = description
        self.price = float(price)

    def __str__(self):
        return f'{self.stockid},{self.name},{self.description},{self.price}'
'''
    def get_id(self):
        return self.stockid

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def set_id(self, new_stockid):
        self.stockid = int(new_stockid)

    def set_name(self, new_name):
        self.name = new_name
    
    def set_description(self, new_desc):
        self.description = new_desc
    
    def set_price(self, new_price):
        self.price = float(new_price)
'''
    
    
def main():
    item1 = Stock('0001','Carrot','Vegetable','0.50')
    item2 = Stock('0002','Strawberry','Fruit','1.50')
    '''
    print(item1.get_id())
    print(item1.get_name())
    print(item1.get_description())
    print(item1.get_price())

    item2.set_id('1476')
    item2.set_name('Harold')
    item2.set_description('Person')
    item2.set_price('9.99')
    '''
    print(item2.__str__())

if __name__ == '__main__':
    main()