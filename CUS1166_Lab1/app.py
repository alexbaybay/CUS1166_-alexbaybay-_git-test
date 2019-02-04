from mymodules.models import Student #imports Student class from models
from mymodules.math_utils import average_grade #imports average_grade method from math_utils

#start of main class
#using user input to store studetn innformation in Roster.
def main():
#    info = " "
#    roster = []
#code should run until user enters quit.
#    while(info != 'quit'):
#        info = input("Enter student name. If done please enter 'quit': ")
#        grade = input("Enter Grade for student: ")
#        student_info = Student(info, set_grade(grade))
#        roster = [student_info]
    info_1 = Student("Frances", 89)
    info_2 = Student("Alex", 97)
    info_3 = Student("Chris", 85)
    info_4 = Student("Ferdinand", 78)
    info_5 = Student("Francisco", 100)
    info_6 = Student("Myrna", 75)
    info_7 = Student("Selina", 83)
    info_8 = Student("Rich", 88)
    info_9 = Student("Richard", 94)
    info_10 = Student("Isabell", 89)

    roster = [info_1,info_2, info_3,info_4,info_5,info_6,info_7,info_8,info_9,info_10]

    for student in roster:
        student.print_student_info()

    average = average_grade(roster)
    print(f"Roster's average score is {average}")

if __name__ == '__main__':
    main()
