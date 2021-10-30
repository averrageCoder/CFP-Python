import random

IS_PRESENT = 1
IS_ABSENT = 0
IS_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

# UC1
attendance = random.randint(0, 2)
if attendance == IS_PRESENT:
    print("Employee is present")
    daily_wage = FULL_DAY_HOUR * WAGE_PER_HOUR
# UC3
elif attendance == IS_PART_TIME:
    print("Employee is available part time")
    daily_wage = PART_TIME_HOUR * WAGE_PER_HOUR
else:
    print("Employee is absent!")
    daily_wage = 0

# UC2
print("Employee Wage: {}".format(daily_wage))
