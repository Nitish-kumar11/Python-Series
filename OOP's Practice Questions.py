# Q.  Creat student calss that takes name & marks of three subjects as arguments in constructor. Then creat a methon to print the average.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def print_average(self):
        average= (self.marks1+self.marks2+self.marks3)/3
        print("Student name is:", self.name)
        print("Student average marks are :", average )

student1= Student("Nitish", 89, 97, 79)
student1.print_average()
print()




''' Q.  1> create account class with 2 attributes-balance & account number.
        2> creatw mwthods for debit, credit and printing the balance'''
class Account:
    # Constructor 
    def __init__(self, bal, acc):
        self.balance = bal          
        self.account_no = acc        

    # Method to deduct (debit) 
    def debit(self, amount):
        self.balance -= amount       
        print("RS", amount, "was debited")   # Display debit info
        print("Total balance is=", self.get_balance())  # Show updated balance

    # Method to add (credit) 
    def credit(self, amount):
        self.balance += amount      
        print("RS", amount, "was credited")   # Display credit info
        print("Total balance is=", self.get_balance())  # Show updated balance

    # Method to return the current balance
    def get_balance(self):
        return self.balance          


Acc1 = Account(4327, 69236489276)
Acc1.debit(1199)
Acc1.credit(1473)






