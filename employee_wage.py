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
    daily_wages = {}
    while total_working_hours <= employee.max_hours_per_month and total_working_days < employee.num_of_working_days:
        total_working_days += 1
        attendance = random.randint(0, 2)
        if attendance == IS_PRESENT:
            # print("Employee is present")
            total_working_hours += FULL_DAY_HOUR
            daily_wage = FULL_DAY_HOUR * employee.emp_rate_per_hour
        # UC3
        elif attendance == IS_PART_TIME:
            # print("Employee is available part time")
            total_working_hours += PART_TIME_HOUR
            daily_wage = PART_TIME_HOUR * employee.emp_rate_per_hour
        else:
            # print("Employee is absent!")
            daily_wage = 0

        daily_wages[total_working_days] = daily_wage
        total_wage += daily_wage

    print("Total Hours: {} Total Wage : {}".format(total_working_hours, total_wage))
    return total_wage, daily_wages


def computeEmpWage(employees):
    updated_employees_list = []
    for employee in employees:
        total_wage, daily_wages = computeWage(employee)
        employee.set_total_emp_wage(total_wage)
        employee.set_daily_wage_dict(daily_wages)
        print(employee)
        updated_employees_list.append(employee)
    return updated_employees_list


def getTotalWageByCompany(company, employees):
    company_total_wage = 0
    for employee in employees:
        if employee.company == company:
            company_total_wage += employee.get_total_wage()

    print("Total employee wages for {} is: {}".format(company, company_total_wage))


if __name__ == "__main__":
    employees = []
    dmart_employee = CompanyEmployeeWage("DMart", 20, 15, 50)
    reliance_employee1 = CompanyEmployeeWage("Reliance", 10, 20, 70)
    reliance_employee2 = CompanyEmployeeWage("Reliance", 10, 20, 70)

    employees.append(dmart_employee)
    employees.append(reliance_employee1)
    employees.append(reliance_employee2)
    employees = computeEmpWage(employees)

    getTotalWageByCompany("Reliance", employees)
