"""Type checking"""


def add_numbers(number_one: int, number_two: int) -> int:
    """Returns the sum of two numebers"""
    return number_one + number_two


result = add_numbers(23, "Hello")

print(result)
