# class Access:

#     def carDoor(self):
#         print("Open the car door sit inside")
#         self._accelerator()

#     def _accelerator(self):
#         print("press the acceleraot to move the car")
#         self.__engineen()

#     def __engineen(self):
#         print("V12 engineen")

# a=Access()
# a.carDoor()


# class company:

#     def __init__(self):
#         self.__companyName="Ocean Academy"

# c=company()


# class ATM:

#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
        
#     def checkBalance(self):
#         print("Bank Balance :",self.__balance)

#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Amount Deposit :",amount)

#     def withdraw(self,amount):

#         if amount <= self.__balance:

#             self.__balance-=amount

#             print("Withdraw amount :",amount)

#         else:
#              print("Insufficient Balance")
    
# a=ATM("Joe",50000)
# a.checkBalance()

# a.deposit(2000)
# a.checkBalance()

# a.withdraw(1000000)
# a.checkBalance()
