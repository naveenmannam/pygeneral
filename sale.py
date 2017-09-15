

NUMBER_OF_DAYS = 5


def sales():
    """
    Returns the sales for 5 days
    """

    lists = [0] * NUMBER_OF_DAYS
    for i in range(NUMBER_OF_DAYS):
        lists[i] = int(input("Enter the amount : "))

    for i in range(len(lists)):
        print(f"Day {i} : ${lists[i].00}")


sales()
