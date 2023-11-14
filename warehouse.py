from stock import Stock
from customer import Customer

from random import randint

class Warehouse:
    def __init__(self) -> None:
        self.stock_items = []
        self.customer_records = []
        self.stock_file = 'stock.txt'
        self.customer_file = 'customers.txt'

    def create_stock_item(self, name, description, price):
        duplicate = True
        stock_ID = -1

        while duplicate:
            duplicate = False

            stock_ID = randint(0, len(self.stock_items))

            for item in self.stock_items:
                if stock_ID == item.stockid:
                    duplicate = True

        new_stock_item = Stock(stock_ID, name, description, price)
        self.stock_items.append(new_stock_item)


    def print_stock_list(self):
        for item in self.stock_items:
            print(item.__str__())

    def write_stock_to_file(self):
        try:
            open_file = open(self.stock_file, 'w')

        except OSError:
            print('FILE NOT FOUND')

        else:
            for item in self.stock_items:
                new_line = item.__str__() + '\n'
                open_file.write(new_line)

            open_file.close()

    def read_stock_from_file(self):
        try:
            open_file = open(self.stock_file, 'r')
        
        except OSError:
            print('FILE NOT FOUND')

        else:
            self.stock_items = []

            for line in open_file:
                read_line = line.rstrip()
                read_line = read_line.split(',')

                stock_name = read_line[1]
                stock_desc = read_line[2]
                stock_price = float(read_line[3])

                self.create_stock_item(stock_name, stock_desc, stock_price)

        open_file.close()


    def create_customer_item(self, fname, sname, address):
        duplicate = True
        customer_ID = -1

        while duplicate:
            duplicate = False

            customer_ID = randint(0, len(self.customer_records))

            for item in self.customer_records:
                if customer_ID == item.customerid:
                    duplicate = True

        new_customer_record = Customer(customer_ID, fname, sname, address)
        self.customer_records.append(new_customer_record)


    def print_customer_list(self):
        for item in self.customer_records:
            print(item.__str__())

    def write_customer_to_file(self):
        try:
            open_file = open(self.customer_file, 'w')

        except OSError:
            print('FILE NOT FOUND')

        else:
            for item in self.customer_records:
                new_line = item.__str__() + '\n'
                open_file.write(new_line)

            open_file.close()

    def read_customer_from_file(self):
        try:
            open_file = open(self.customer_file, 'r')
        
        except OSError:
            print('FILE NOT FOUND')

        else:
            self.customer_records = []

            for line in open_file:
                read_line = line.rstrip()
                read_line = read_line.split(',')

                customer_fname = read_line[1]
                customer_sname = read_line[2]
                customer_address = read_line[3]

                self.create_customer_item(customer_fname, customer_sname, customer_address)

        open_file.close()

        


if __name__ == '__main__':
    new_warehouse = Warehouse()

    # new_warehouse.create_stock_item('carrot', 'vegetable', 0.99)
    # new_warehouse.create_stock_item('potato', 'vegetable', 0.99)
    # new_warehouse.create_stock_item('asparagus', 'vegetable', 0.99)
    # new_warehouse.create_stock_item('swede', 'vegetable', 0.99)

    # new_warehouse.print_stock_list()

    # new_warehouse.write_stock_to_file()

    # new_warehouse.read_stock_from_file()

    new_warehouse.create_customer_item('Jim', 'Jones', '14 test st')
    new_warehouse.create_customer_item('Tim', 'Jones', '14 test st')
    new_warehouse.create_customer_item('Lim', 'Jones', '14 test st')
    new_warehouse.create_customer_item('Pim', 'Jones', '14 test st')

    new_warehouse.print_customer_list()

    new_warehouse.write_customer_to_file()

    new_warehouse.read_customer_from_file()
