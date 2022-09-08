'''Week 12 Checkpoint - Using Objects'''
'''An object has data (attributes) and functions (methods) 
and that a programmer uses the dot operator (.) to access 
the attributes and call the methods in an object. Python lists 
and dictionaries are objects and contain attributes and methods.'''


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f'Reverse: {fruit_list}')

    # Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append('orange')
    print(f'Add orange: {fruit_list}')

    # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    index = fruit_list.index('apple')
    print(f'Apple index: {index}')
    fruit_list.insert(1, 'cherry')
    print(f'Cherry before apple: {fruit_list}')

    # Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove('banana')
    print(f'Remove banana: {fruit_list}')

    # Add code to pop the last element from fruit_list and print the popped element and the list.
    last_item = fruit_list.pop()
    print(f'Popped fruit: {last_item}')

    # Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f'Sorted list: {fruit_list}')

    # Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f'Cleared list: {fruit_list}')


if __name__ == "__main__":
    main()
