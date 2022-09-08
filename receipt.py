'''Week 09 - 10 Prove'''

import csv
from os import read
from datetime import datetime
import random
from typing import final


def read_products(filename):
    '''Reads csv file '''
    #  creates dictionary
    products = {}
    try:
        # opens and reads file
        with open(filename, "rt") as prod_file:
            # creates reader to read to csv
            reader = csv.reader(prod_file)
            # skips first line
            next(reader)

            # csv have rows that reader reads as lists
            for row in reader:
                # From the current row, retrieve
                # the column that contains the key.
                num_key = (row[0])
                # Store the data from the current row
                # into the dictionary.
                products[num_key] = (row[1], row[2])

                # key = 'D150' value = ["1 gallon milk", 2.85]

        return products

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)


def main():
    try:
        products_dict = read_products('products.csv')
        # print('Products')
        # print(products_dict)
        print()

        with open('request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)

            print('Inkom Emporium')
            print()
            # print('Requested Items')
            num_items = 0
            subtotal_price = 0
            subtotal = 0

            for row in reader:
                request_product = row[0]
                product_name = products_dict[request_product][0]
                quantity = int(row[1])  # int so it doesn't reads it as str
                price = float(products_dict[request_product][1])

                print(f'{product_name}: {quantity} @ {price}')

                num_items += quantity
                subtotal_price += price
                subtotal_product = price * quantity
                subtotal += subtotal_product
                tax = subtotal * 0.06
                total = subtotal + tax

        print()
        print(f'Number of Items: {num_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {tax:.2f}')
        print(f'Total: {total:.2f}')

        print()
        guess = input(
            'Would you like to guess a number to obtain a discount? y/n: ')
        if guess == 'y':
            number = int(input('Guess a number between 1 and 10: '))
            guess_number = random.randint(1, 10)

            if number == guess_number:
                print('You got 10%' 'discount!')
                discount = total * 0.1
                final_total = total - discount
                print(f'Your total is: {final_total:.2f}')

            else:
                print('Try again next time!')

        elif guess == 'n':
            print('See you next time!')

    except FileNotFoundError as not_found_err:
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)

    except TypeError as type_err:
        print(type_err)

    except ValueError as val_err:
        print(val_err)

    # Call the now() method to get the current date and
    # time as a datetime object from the computer's clock.
    current_date_and_time = datetime.now()
    weekday = current_date_and_time.weekday()

    if weekday == 3:
        print(f'You are lucky! You got 15% discount on your next purchase! \nShow this receipt.')

    print()
    print('Thank you for coming at the Inkom Emporium. Happy Shopping!')

    # Print the current day of the week and the current time.
    # weekday month num_day hour:min pm year
    print(f"{current_date_and_time:%a %b %d %I:%M %p %Y}")


if __name__ == "__main__":
    main()
