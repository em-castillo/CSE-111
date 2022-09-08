'''Week 11 Team Assignment'''

import csv
from os import read


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    # call read_compound_list() to read pupils.csv into students_list
    students_list = read_compound_list("pupils.csv")

    # lambda function to extract birthday from a student
    def birthday_func(birthday): return birthday[BIRTHDATE_INDEX]

    def given_name_func(student_list): return \
        f"{student_list[GIVEN_NAME_INDEX]}, {student_list[SURNAME_INDEX]}"

    # sorted function to sort students_list by birthdate
    # oldest to youngest
    birthday_sort = sorted(students_list, key=birthday_func)
    print("\nOrdered from Oldest to Youngest")
    for student in birthday_sort:
        print(student)

    # given_name
    given_name_sort = sorted(students_list, key=given_name_func)
    print("\nOrdered by First Name")
    for name in given_name_sort:
        print(name)

    month_day = sort_by_birth_month_day(students_list)
    print('\nOrdered by Birth Month and Day')
    print_list(month_day)


# Birthday Month Day
def sort_by_birth_month_day(students_list):
    def extract_month_and_day(student):
        birthdate_string = student[BIRTHDATE_INDEX]
        month_and_day = birthdate_string[5:]
        return month_and_day

    # Call the sorted function to sort the list
    # of students by their birth month and day.
    sorted_list = sorted(students_list, key=extract_month_and_day)

    # Return the sorted list.
    return sorted_list


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(compound_list):
    for item in compound_list:
        print(item)


if __name__ == "__main__":
    main()
