a = 5
b = 0

try:
    # c = a / b
    raise ZeroDivisionError("Explicitly raised an exception!")
except Exception as exception:
    print(exception.__str__())
    print(exception.__traceback__)
finally:
    print("try except successfully completed")
