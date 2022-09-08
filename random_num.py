'''Week 07 Team Activity'''
"""
Write and call functions that demonstrate both
default parameter values and pass by reference.
"""




from random import uniform, choice # or import random
def main():
    # create list
    randwords = ['apple', 'banana', 'blackberries', 'cantalupe', 'grapes', 'kiwi',
                 'lemon', 'lime', 'melon', 'orange', 'pineapple', 'raspberries', 'strawberries']

    randnums = [16.2, 75.1, 52.3]

    # print randnums list
    print(randnums)
    # call append_random_numbers function with 1 argument: randnums
    append_random_numbers(randnums)
    # print randnums
    print(randnums)
    # call append_random_numbers function with 2 argument (add 3 numbers to randnums)
    append_random_numbers(randnums, 3)
    # print
    print(randnums)

    print(randwords)
    append_random_words(randwords, 3)
    print(randwords)


def append_random_numbers(numbers_list, quantity=1):
    '''It has two parameters: a list named numbers_list and an integer named quantity. 
    The parameter quantity has a default value of 1'''
    for i in range(1, quantity + 1):
        # random.uniform function generates random numbers that are not integers.
        num = uniform(1, 100)
        #  round function rounds a number to a specified number of digits after the decimal place.
        num = round(num, 1)
        # append to list
        numbers_list.append(num)

# Stretch challenge


def append_random_words(words_list, quantity=1):
    # Randomly choose quantity words and append them onto words_list.
    for i in range(1, quantity + 1):
        word = choice(words_list)
        words_list.append(word)


if __name__ == "__main__":
    main()
