# pass_args.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.
'''Week 07 Checkpoint'''

"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""


def main():
    print("main()")
    # local variables
    x = 5
    lx = [7, -2]
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters:
        n - A number
        alist - A list
    Return: nothing
    """
    print("    modify_args(n, alist)")
    print(f"        Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"        After changing n and alist:  n {n}  alist {alist}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()


'''Notes 
array: same type of items
list: different types of items
dictionary: key/values pairs, no order guaranted
list.insert[0, 'Billie'] -> adds item before index specified
list.sort -> in abc order
variable = list[1:3] -> start and end index(from 1 without including 3)
dictionaries -> person = {'first': 'Chris'}
                person['last'] = 'Harrison' -> add to the dictionary
                print(person) -> {'first': 'Chris', 'last': 'Harrison'}

'''
