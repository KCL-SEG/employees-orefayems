"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
employees = []
class Employee:
	def __init__(self, name, salary, rate, totalTime, commissionContractsss, commissionPay, description):
        self.name = name
		self.commissionPay = commissionPay
		self.description = description
        self.rate = rate
		self.commissionContracts = commissionContracts
		self.totalTime = totalTime
		self.salary = salary
		self.getPay()
		self.__str__()

	def getPay(self):
		totalPay = (self.salary * self.totalTime) + (self.commissionContracts * self.commissionPay)
		if self.commissionContracts == 0 and self.commissionPay == 0;
			totalpay = (self.salary * self.totalTime)
		if self.commissionContracts == 0 and self.commissionPay > 0;
			totalpay = (self.salary * self.totalTRIme) + self.commissionPay
		return totalpay

	def __str__(self):
		return self.description

	# Billie works on a monthly salary of 4000.  Their total pay is 4000.
	billie = Employee('Billie', 4000, "monthly", 1,0,0, 'Billie works on a monthly salary of 4000. Their total pay is 4000.')


	# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
	charlie = Employee('Charlie', 25, "hourly", 100,0,0, 'Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.')

	# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
	renee = Employee('Renee', 3000, "monthly", 1,4,200, 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3000.')

	# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
	jan = Employee('Jan', 25, "hourly", 150,3,220, 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contact. Their total pay is 4410.')

	# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
	robbie = Employee('Robbie', 2000, "monthly", 1,0,1500, 'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.')
	# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.

	ariel = Employee('Ariel', 30, "hourly", 120,0,600, 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.')
