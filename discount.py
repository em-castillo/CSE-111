from datetime import datetime

subtotal = float(input('Please enter the subtotal: '))

date = datetime.now()  # current day and time
weekday = date.weekday()
weekday = 2  # to see if discount applies

ten_percent = 0
discount = 0
tax = 0
total = 0

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = subtotal * 0.1
    tax = (subtotal - discount) * 0.06
    total = (subtotal - discount) + tax
    print(f'Discount amount: {discount:.2f}')

else:
    difference = 50 - subtotal
    tax = subtotal * 0.06
    total = subtotal + tax
    print(f'Spend ${difference} to have a discount')


print(f'Sales tax amount: {tax:.2f}')
print(f'Total: {total:.2f}')
