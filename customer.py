class Customer:
    def __init__(self, customerid, fname, sname, address):
        self.customerid = int(customerid)
        self.fname = fname
        self.sname = sname
        self.address = address

    def __str__(self):
        return f'{self.customerid},{self.fname},{self.sname},{self.address}'

    def get_id(self):
        return self.customerid

    def get_fname(self):
        return self.fname
    
    def get_sname(self):
        return self.sname
    
    def get_address(self):
        return self.address
    
    def set_id(self, new_customerid):
        self.customerid = int(new_customerid)

    def set_fname(self, new_fname):
        self.fname = new_fname
    
    def set_sname(self, new_sname):
        self.sname = new_sname
    
    def set_address(self, new_address):
        self.address = new_address

    
    
def main():
    cust1 = Customer('0001', 'Carrot', 'Vegetable', '0.50')
    cust2 = Customer('0002', 'Strawberry', 'Fruit', '1.50')

    print(cust1.get_id())
    print(cust1.get_fname())
    print(cust1.get_sname())
    print(cust1.get_address())

    cust2.set_id('1476')
    cust2.set_fname('Harold')
    cust2.set_sname('Person')
    cust2.set_address('9.99')

    print(cust2.__str__())

if __name__ == '__main__':
    main()