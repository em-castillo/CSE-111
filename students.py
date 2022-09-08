'''Week 09 Team Activity'''

import csv


def main():

    # Indexes of students.csv
    INUMBER_INDEX = 0
    STUDENT_NAME_INDEX = 1

    # reads content of csv. Uses I-number as key in dictionary.
    students = read_dict("students.csv", INUMBER_INDEX)

    # user's input
    usr_i_number = input("Please enter an I-Number (xxxxxxxxx): ")

    # removes dashes from I-number
    i_number = usr_i_number.replace("-", "")

    # if I-number is longer
    if len(i_number) > 9:
        print(f"Invalid I-Number: too many digits")

    # if I-number is shorter
    elif len(i_number) < 9:
        print(f"Invalid I-Number: too few digits")

        # if I-number is present
        if i_number in students:
            print(f"{students[i_number]}")
        # if not in dictionary
        else:
            print("No such student")
    else:
        print("Invalid I-Number")


def read_dict(filename, key_column_index):
    '''Reads dictionary created from csv file'''

    # creates dictionary
    students = {}

    # opens and reads file
    with open(filename, "rt") as csv_file:
        # creates reader to read to csv
        reader = csv.reader(csv_file)
        # skips first line
        next(reader)

        # csv have rows that reader reads as lists
        for row in reader:
            # reads the key of the row -> I-number
            key = row[key_column_index]
            # stored data to dictionary -> Student's name
            students[key] = row  # [1]

    return students


if __name__ == "__main__":
    main()
