class CompanyEmployeeWage:
    """
    Class to store company employee wage

    Attributes:
        company: name of the company
        emp_rate_per_hour: employee rate per hour
        num_of_working_days: max number of working days
        max_hours_per_month: max hours per month
    """

    def __init__(self, company, emp_rate_per_hour, num_of_working_days, max_hours_per_month):
        """
        Constructor to initialize the object
        :param company: name of the company
        :param emp_rate_per_hour: employee rate per hour
        :param num_of_working_days: max number of working days
        :param max_hours_per_month: max hours per month
        """
        self.company = company
        self.emp_rate_per_hour = emp_rate_per_hour
        self.num_of_working_days = num_of_working_days
        self.max_hours_per_month = max_hours_per_month

    def set_total_emp_wage(self, total_emp_wage):
        """
        Method to set the total employee wage
        :param total_emp_wage: total employee wage
        :return: None
        """
        self.total_emp_wage = total_emp_wage

    def get_total_wage(self):
        """
        Method to return the total employee wage
        :return: total employee wage
        """
        try:
            return self.total_emp_wage
        except Exception as e:
            print(e.__str__())
            return 0

    def set_daily_wage_dict(self, daily_wages):
        """
        Method to store daily wages mappings
        :param daily_wages: diction with daily wages
        :return: None
        """
        self.daily_wages = daily_wages

    def __str__(self):
        """
        String version of the class object
        :return: object details as a string
        """
        string = ""
        for key, value in self.daily_wages.items():
            string += "\n Day: {} Wage: {}".format(key, value)
        string += "\n Total employee wage for company: " + str(self.company) + " is: " + str(self.total_emp_wage)
        return string
