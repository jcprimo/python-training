#Python OOP
import datetime
class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@yoMero.com'
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

#At this point the counter is at 0 because we havent created any employees
print("Total number of employees: ", Employee.num_of_emps)

emp_1 = Employee('Yo', 'Mero', 95000)
emp_2 = Employee('El', 'Loco', 60000)

# Updates the raise amount given raise amount
Employee.set_raise_amt(1.03)

#Example of using @classmethod decorator for an alternative contructor
emp_str_1 = 'Juana,Perez,45000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

#using staticmehtods to check if it is a work day given a number
my_date = datetime.date(2020, 5, 26)
print(Employee.is_workday(my_date))

# At this point the counter is =2 because we have created two employees
print("Total number of employees: ", Employee.num_of_emps)
