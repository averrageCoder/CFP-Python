class CompanyEmployeeWage:
    def __init__(self, company, empRatePerHour, numOfWorkingDays, maxHoursPerMonth):
        self.company = company
        self.empRatePerHour = empRatePerHour
        self.numOfWorkingDays = numOfWorkingDays
        self.maxHoursPerMonth = maxHoursPerMonth

    def setTotalEmpWage(self, totalEmpWage):
        self.totalEmpWage = totalEmpWage;

    def __str__(self):
        return "Total employee wage for company: "+self.company+" is: "+self.totalEmpWage