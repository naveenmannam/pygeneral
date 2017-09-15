"""Salary calculation for employees"""


def calculate_salary():
    """Returns the total amount of salary
    needed to be payed to the employees
    on per hour basics of working
    """

    number_of_emp = int(input("Employee count : "))

    # emp = [0] * number_of_emp
    per_hour_rate = 12.50
    amount = []
    for i in range(number_of_emp):
        hours = int(input(f"Enter hours worked for employee {i + 1} : "))
        amount.append(hours * per_hour_rate)

    total_amount = 0
    for i in range(len(amount)):
        print(f"Salary for employee {i + 1} is : ${amount[i]}")
        total_amount += amount[i]

    print("-----------------------------")
    print(f"Total Salary             : ${total_amount}")


calculate_salary()
