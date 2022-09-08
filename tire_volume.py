import math
from datetime import datetime

print('Welcome!')

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60):  '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))


parenthesis = width * ratio + 2540 * diameter
top_formula = math.pi * width**2 * ratio * parenthesis
volume = top_formula / 10000000000

print(f'The approximate volume is {volume:.2f} liters')

# part 2

if width < 100 and ratio < 14 and diameter <= 17:
    print('Price of tire with the dimensions entered is $389.99 each.')

elif (width >= 100 and width <= 200) and (ratio >= 35 and ratio <= 70) and (diameter <= 17):
    print('Price of tire with the dimensions entered is $109.99 each.')

elif (width > 200) and (ratio >= 30 and ratio <= 75) and (diameter <= 17):
    print('Price of tire with the dimensions entered is $114.99 each.')

else:
    print('Please call us for more information.')


buy_tires = input(
    'Do you want to buy tires with the dimensions entered? (yes/no): ')

phone = 0
name = '-'

if buy_tires == 'yes':
    name = input('Enter your name: ')
    phone = int(input('Please enter your phone number: '))
    print('Thank you. We will contact you soon.')

else:
    print('Thank you. Have a good day.')


date = datetime.now()


# at appending to the end of a text file.
with open('volumes.txt', mode='at') as volume_file:
    print(f'{date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {name}, {phone}', file=volume_file)
