#must accept list of student objects
#had help from Selina Mangaroo
def average_grade(roster):
    sum = 0
    for student in roster:
        sum += student.get_grade()
    average = sum/len(roster)
    return average

def main():
    pass

if __name__== "__main__":
    main()
