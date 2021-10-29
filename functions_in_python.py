def square():
    numbers_list = [1, 3, 5, 7, 9]
    for num in numbers_list:
        print(num * num, end=" ")


def empty_function():
    pass


def variable_arguments(*params1, **params2):
    print(params1)
    print(params2)


if __name__ == "__main__":
    square()
    empty_function()
    numbers = [1, 3, 5, 7, 9]
    variable_arguments(numbers, key1="value1", key2="value2")
