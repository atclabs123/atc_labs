import os
import sys


def read_file(file_name):
    try:
        lines = []
        with open(file_name, "r") as file:
            lines = file.readlines()
        return lines

    except FileNotFoundError:
        print("File does not exist, please use option 2 first and add a new student")


def write_file(file_name, list):
    with open(file_name, "w") as file:
        file.writelines(list)


def display_grades(file_name):
    try:
        lines = read_file(file_name)
        for line in lines:
            name, grade = line.strip().split("|")
            print(f"{name} - {grade}")

    except Exception as e:
        print(f"display_grades failed {e}")
        sys.exit(1)


def add_new_student(file_name):
    name = input("Enter the student name: \n").strip()
    grade = input(f"Enter the {name} grade: \n").strip()

    with open(file_name, "a") as file:
        file.write(f"{name}|{grade}\n")

    print(f"{name} added successfully")


def update_student_grade(file_name):
    name = input("Enter the student name whose grade you want to change\n").strip()
    lines = read_file(file_name)

    found = False
    new_grade = ""
    i = 0
    for line in lines:
        print(line.strip())
        student_name_from_file = line.strip().split("|")[0]

        if name == student_name_from_file:
            found = True
            print(f"{name} found in the grades")
            new_grade = input("Enter the new grade input: \n").strip()

            lines[i] = f"{name}|{new_grade}\n"
            break
        i += 1

    if not found:
        print(f"{name} not found in the grades")
    else:
        # name found
        write_file(file_name, lines)
        print("Grade updated successfully")


def calculate_average_grade(file_name):
    lines = read_file(file_name)
    marks = [int(line.strip().split("|")[1]) for line in lines]

    # for line in lines:
    #     marks = int(line.strip().split("|")[1])

    no_of_marks = len(marks)
    sum_of_marks = sum(marks)

    try:
        average_marks = float(sum_of_marks / no_of_marks)

    except ZeroDivisionError:
        print("Add student and grades first")

    print("Class Average is : ", average_marks)


# explaination for     marks = [int(line.strip().split("|")[1]) for line in lines ]
#     ["afsar|92", "yaseen|89", "aneesa|91"]

#     "afsar|92" ->  "afsar|92" -> ["afsar","92"] -> 92
#     "yaseen|89"->  "yaseen|89" -> ["yaseen","89"] -> 89
#     "aneesa|91"->  "aneesa|91" -> ["aneesa","91"] -> 91

# [92, 89, 91]


def main():
    while True:
        print("\n1. Display Grades")
        print("\n2. Add New Student")
        print("\n3. Update Student Grades")
        print("\n4. Calculate Average Grades")
        print("\n5. Exit the program")

        file_name = "grades.txt"

        choice = int(input("\nEnter your choice\n").strip())
        print("Selected Choice: ", choice)

        if choice == 1:
            print("display grade")
            display_grades(file_name)

        elif choice == 2:
            print("add new student")
            add_new_student(file_name)

        elif choice == 3:
            print("update student grade")
            update_student_grade(file_name)

        elif choice == 4:
            print("calculate average grade")
            calculate_average_grade(file_name)

        elif choice == 5:
            print("Exiting the program")
            break

        else:
            print("Invalid Choice\n")


if __name__ == "__main__":
    main()
