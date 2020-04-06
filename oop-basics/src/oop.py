#Python OOP
import datetime
class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@ElChingon.com'
		#within the init, add+1 to the counter employee
		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		#In order to access class variables within the class then add self
		self.pay = int(self.pay * self.raise_amt)

	#Updates the amount of the raise per the class object
	@classmethod #This is called DECORATOR
	def set_raise_amt(cls, amount):
		cls.raise_amt=amount

	#Alternative constructor to create a new employee instance
	#Example of using classmethods as alternative constructors
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split(",")
		return cls(first, last, pay)

	# Static methods do not operate on the instance or the class
	# They are independent
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

#Create a new class to demonstrate subclassing
class Developer(Employee):
	#Through inheritance, Developer class can access all the methods from Employee class
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		#Declaring the constructor without code repetition
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

# New class where it takes as parameter a list of employees
class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		#Declaring the constructor without code repetition
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--> ', emp.fullname())

#At this point the counter is at 0 because we havent created any employees
print("Total number of employees: ", Employee.num_of_emps)

dev_1 = Developer('Yo', 'Mero', 95000, 'Python')
dev_2 = Developer('El', 'Loco', 60000, 'React')
mgr_1 = Manager('El', 'Patron', 125000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)

print("Manager in charge of: ")
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)

print("\nAfter removal")
mgr_1.print_emps()

# Updates the raise amount given raise amount
Employee.set_raise_amt(1.03)

#Example of using @classmethod decorator for an alternative contructor
emp_str_1 = 'Juana,Perez,45000'
new_emp_1 = Employee.from_string(emp_str_1)

print(dev_1.pay)
dev_1.apply_raise()

#using staticmehtods to check if it is a work day given a number
my_date = datetime.date(2020, 5, 26)
#print(Employee.is_workday(my_date))

# At this point the counter is =2 because we have created two employees
print("Total number of employees: ", Employee.num_of_emps)
