'''Week 09 Checkpoint - Text Files'''


def read_file(provinces):
    '''Reads the text file'''
    provinces_list = []
    # Open the provinces.txt file for reading.
    # It doesn't need to close later because of the word 'with'
    with open(provinces, 'rt') as file:

        # Read the contents of the file into a list where each line of
        # text in the file is stored in a separate element in the list.
        for line in file:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()
            # Append the clean line of text
            # onto the end of the list.
            provinces_list.append(clean_line)

    return provinces_list


def main():
    # Read the contents of a text file
    # named provinces.txt into a list
    provinces_list = read_file('provinces.txt')

    # Print the entire list.
    print(provinces_list)
    # Remove the first element from the list.
    provinces_list.pop(0)

    # Remove the last element from the list.
    provinces_list.pop()

    # Replace all occurrences of "AB" in the list with "Alberta".
    for i in range(len(provinces_list)):
        # if list index == 'AB'
        if provinces_list[i] == 'AB':
            # Replace AB with Alberta.
            provinces_list[i] = 'Alberta'

    # Count the number of elements that are "Alberta" and print that number.
    if 'Alberta' in provinces_list:
        count = provinces_list.count('Alberta')

    print(f'Alberta occurs {count} times in the modified list.')


# Call main to start this program.
if __name__ == "__main__":
    main()
