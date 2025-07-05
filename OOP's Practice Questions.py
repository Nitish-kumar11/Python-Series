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





# Q.  create account class with 2 attributes-balance & account number. 

class Account :
    def __init__(self,bal, acc ):
        self.balance=bal
        self.account_no=acc

    def debit(slef, amount):
        slef.balance-=Account
        print("RS:",amount, "was debited")

    def credit(slef, amount):
        slef.balance-=Account
        print("RS:",amount, "was debited")

Acc1= Account(4327, 69236489276)   
print("Your current account balance is:",Acc1.balance)   
print("Your accounut number is:",Acc1.account_no) 