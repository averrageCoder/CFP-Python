class CompanyEmployeeWage:
    def __init__(self, company, empRatePerHour, numOfWorkingDays, maxHoursPerMonth):
        self.company = company
        self.empRatePerHour = empRatePerHour
        self.numOfWorkingDays = numOfWorkingDays
        self.maxHoursPerMonth = maxHoursPerMonth

    def setTotalEmpWage(self, totalEmpWage):
        self.totalEmpWage = totalEmpWage

    def getTotalWage(self):
        try:
            return self.totalEmpWage
        except Exception as e:
            print(e.__str__())
            return 0

    def setDailyWageDict(self, dailyWages):
        self.dailyWages = dailyWages

    def __str__(self):
        string = ""
        for key, value in self.dailyWages.items():
            string += "\n Day: {} Wage: {}".format(key, value)
        string += "\n Total employee wage for company: " + str(self.company) + " is: " + str(self.totalEmpWage)
        return string
