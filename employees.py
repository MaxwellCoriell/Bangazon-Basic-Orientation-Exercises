class Company(object):
    '''
    Contains methods for employee tracking in a company

    Methods
    =======

    get_name
    get_job_title
    get_start_date
    '''

    def __init__(self, company_name, employees=[]):
        self.name = company_name
        self.employees = employees
        

    def add_employee(self, employee):
        self.employees.add(employee)

    def get_employees(self):
        return self.employees

    def __str__(self):
        employee_list = '{} Employee List\n-------------------------'.format(self.name)
        for employee in self.employees:
            employee_list += '\n{}'.format(employee)
        return employee_list

    # Add the remaining methods to fill the requirements above

class Employee(object) :
	'''
    Contains methods for employee information
    Methods
    =======
    get_name
    set_job_title
    get_job_title
    set_start_date
    get_start_date
    '''

	def __init__(self, first_name, last_name, job_title="The Brawn", start_date="1 JUN 2015"):
		self.first_name = first_name
		self.last_name = last_name
		self.title = job_title
		self.start_date = start_date

	def get_name(self):
		'''
		Returns the employee's name
		'''
		full_name = self.first_name + " " + self.last_name
		return full_name

	def set_job_title(self, job_title):
		self.title = job_title

	def get_job_title(self):
		'''
		Returns the employee's job title
		'''
		return self.title

	def set_start_date(self, start_date):
		self.start_date = start_date

	def get_start_date(self):
		'''
		Returns the employee's start date
		'''
		return self.start_date

	def __str__(self):
		employee_str = '{0}, {1}, started {2}'.format(self.get_name(), self.get_job_title(), self.get_start_date())
		return employee_str

maxwell = Employee("Max", "Baldridge", "The Beard", "3 JAN 2017")
adam = Employee("Adam", "Myers", "The Bashful", "3 JAN 2017")
kayla = Employee("Kayla", "Brewer", "The Beauty", "3 JAN 2017")
steve = Employee("Steve", "Brownlee", "Coach")
john = Employee("John", "Wark", "Founder", "1 JUN 2012")

ginger_employees = [maxwell, adam, kayla, steve, john]

ginger_llc = Company("Ginger, LLC", ginger_employees)

print(ginger_llc)

























