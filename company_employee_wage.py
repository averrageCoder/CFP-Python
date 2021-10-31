class CompanyEmployeeWage:
    def __init__(self, company, empRatePerHour, numOfWorkingDays, maxHoursPerMonth):
        self.company = company
        self.empRatePerHour = empRatePerHour
        self.numOfWorkingDays = numOfWorkingDays
        self.maxHoursPerMonth = maxHoursPerMonth

    def setTotalEmpWage(self, totalEmpWage):
        self.totalEmpWage = totalEmpWage

    def setDailyWageDict(self, dailyWages):
        self.dailyWages = dailyWages

    def __str__(self):
        string = ""
        for key, value in self.dailyWages.items():
            string += "\n Day: {} Wage: {}".format(key, value)
        string += "\n Total employee wage for company: " + str(self.company) + " is: " + str(self.totalEmpWage)
        return string
