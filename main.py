from warehouse import Warehouse
import os
from sys import exit


os.system('cls')

def menu():

    stock_item_count = 0
    customer_record_count = 0
    flag=True

    print('Welcome!')

    while flag:
        print('''Select option:
    1. Stock
    2. Customers
    3. Exit''')

        choice1 = input('Enter your choice: ')

        if choice1 == '1':
            new_warehouse.read_stock_from_file()
        elif choice1 == '2':
            new_warehouse.read_customer_from_file()

        while choice1 == '1':
            print('''Select an option:
    1. Create stock item
    2. Print out stock items
    3. Write new items to file
    4. Exit to main menu
    5. Exit system''')
            
            choice2 = input('Enter your choice: ')

            if choice2 == '1':
                new_stock_name = input('Enter the name of the new item: ')
                new_stock_desc = input('Enter the description of the new stock: ')
                new_stock_price = input('Enter the price of the new stock: ')

                new_warehouse.create_stock_item(new_stock_name, new_stock_desc, new_stock_price)

            elif choice2 == '2':
                new_warehouse.print_stock_list()

            elif choice2 == '3':
                new_warehouse.write_stock_to_file()

            elif choice2 == '4':
                break

            elif choice2 == '5':
                exit()
            
        while choice1 == '2':
            print('''Select an option:
    1. Create customer record
    2. Print out customer records
    3. Write new records to file
    4. Exit to main menu
    5. Exit system''')
            
            choice2 = input('Enter your choice: ')

            if choice2 == '1':
                new_customer_fname = input('Enter the first name of the new customer: ')
                new_customer_sname = input('Enter the surname of the new customer: ')
                new_customer_address = input('Enter the address of the new customer: ')

                new_warehouse.create_customer_item(new_customer_fname, new_customer_sname, new_customer_address)

            elif choice2 == '2':
                new_warehouse.print_customer_list()

            elif choice2 == '3':
                new_warehouse.write_customer_to_file()

            elif choice2 == '4':
                break

            elif choice2 == '5':
                exit()
            
        while choice1 == '3':
            exit()

new_warehouse = Warehouse()

menu()