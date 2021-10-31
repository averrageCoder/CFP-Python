import random
from company_employee_wage import CompanyEmployeeWage

IS_PRESENT = 1
IS_ABSENT = 0
IS_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
WORKING_DAYS_PER_MONTH = 20


def uc1_to_uc5():
    # UC5
    total_wage = 0
    total_working_hours = 0
    total_working_days = 0
    for day in range(1, WORKING_DAYS_PER_MONTH + 1):
        if total_working_hours >= 100 or total_working_days >= 20:
            break
        # UC1
        attendance = random.randint(0, 2)
        if attendance == IS_PRESENT:
            # print("Employee is present")
            total_working_hours += FULL_DAY_HOUR
            total_working_days += 1
            daily_wage = FULL_DAY_HOUR * WAGE_PER_HOUR
        # UC3
        elif attendance == IS_PART_TIME:
            # print("Employee is available part time")
            total_working_hours += PART_TIME_HOUR
            total_working_days += 1
            daily_wage = PART_TIME_HOUR * WAGE_PER_HOUR
        else:
            # print("Employee is absent!")
            daily_wage = 0

        # UC2
        print("Employee Wage For Day {}: {}".format(day, daily_wage))
        total_wage += daily_wage

    print("Total Hours: {} Total Wage : {}".format(total_working_hours, total_wage))


def computeWage(employee):
    total_wage = 0
    total_working_hours = 0
    total_working_days = 0
    while (total_working_hours <= employee.maxHoursPerMonth and total_working_days < employee.numOfWorkingDays):
        attendance = random.randint(0, 2)
        if attendance == IS_PRESENT:
            # print("Employee is present")
            total_working_hours += FULL_DAY_HOUR
            total_working_days += 1
            daily_wage = FULL_DAY_HOUR * employee.empRatePerHour
        # UC3
        elif attendance == IS_PART_TIME:
            # print("Employee is available part time")
            total_working_hours += PART_TIME_HOUR
            total_working_days += 1
            daily_wage = PART_TIME_HOUR * employee.empRatePerHour
        else:
            # print("Employee is absent!")
            daily_wage = 0

        total_wage += daily_wage

    print("Total Hours: {} Total Wage : {}".format(total_working_hours, total_wage))
    return total_wage


def computeEmpWage(employees):
    for employee in employees:
        employee.setTotalEmpWage(computeWage(employee))
        print(employee)


if __name__ == "__main__":
    employees = []
    dmartEmployee = CompanyEmployeeWage("DMart", 20, 2, 10)
    relianceEmployee = CompanyEmployeeWage("Reliance", 10, 4, 20)
    employees.append(dmartEmployee)
    employees.append(relianceEmployee)
    computeEmpWage(employees)
