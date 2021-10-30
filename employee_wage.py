import random

IS_PRESENT = 1
IS_ABSENT = 0
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

# UC1
if random.randint(0, 1) == IS_PRESENT:
    print("Employee is present")
    daily_wage = FULL_DAY_HOUR * WAGE_PER_HOUR
else:
    print("Employee is absent!")
    daily_wage = 0

# UC2
print("Employee Wage: {}".format(daily_wage))
