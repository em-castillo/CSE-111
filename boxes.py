import math

num_items = int(input('Enter the number of items: '))
num_items_box = int(input('Enter the number of items per box: '))
print('')

# The math.ceil() function rounds a number up to the nearest integer that is greater than or equal to a number.
num_boxes = math.ceil(num_items / num_items_box)

print(f'For {num_items} items, packing {num_items_box} items in each box, you will need {num_boxes} boxes.')
