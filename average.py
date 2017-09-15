"""Calculate the average marks scored"""


def calculate_average():
    """Returns the average marks scored by a student"""

    marks = []
    subject_name = input("Subject Name : ")
    num_of_attempts = int(input("Exams Written : "))
    for i in range(num_of_attempts):
        item = int(input(f"Enter marks in attempt {i + 1} : "))
        marks.append(item)

    min_marks = min(marks)
    marks.remove(min_marks)

    total = 0
    for i in range(len(marks)):
        total += marks[i]

    average = total / len(marks)

    print()
    print(f"Average score in {subject_name} is {average}")
    print()


calculate_average()
