######--------CONSTRUCTOR IN PYTHON-------#######

class car:
     # (default constructor)
     def __init__(self):
        pass
    
    # (this is parametrized constructor)
     def __init__(self, name, price ):
        self.brand= name
        self.price= price
        print("adding new car..")
car1= car("BMW", "2.5CR")
print(car1.brand, car1.price)

car2= car("Audi", "2.7CR")
print(car2.brand, car2.price)
print() 


######-----class attributes------######

class car:
    made_in = "India"

    #(this is a parametrized constructor)
    def __init__(self, name, price):
        self.brand = name
        self.price = price
        print("adding new car..")

car1 = car("BMW", "2.5CR")
print(car1.brand, car1.price)
print(car1.made_in)

car2 = car("Audi", "2.7CR")
print(car2.brand, car2.price)
print()



######----ONE MORE CLASS ATTRIBUTE EXAMPLE----######

class student:
    college_name="Cambridge institute of technology"
    name="anonymous" # (class attribute)

    def __init__(self, name , marks):
        self.name=name # (object attribute)
        self.marks=marks

S1=student("Nitish kumar", 81) 
print(S1.name, S1.marks) # (here name does't print anonymous because object attribute > class attribute)
print()






####-----METHODS-------  #####


class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display student details
    def display_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


student1 = Student("Nitish", 23)
student2 = Student("Nicky", 22)


student1.display_info()
print()  # (for spacing)
student2.display_info()
print()





 #####---static---method


class Student:
    @staticmethod #decorator 
    def greet():
        print("Hello,Nitish welcome to the class")


Student.greet()
print()





#####------ABSTRACTION------######

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("Car is Started")

car1=Car()
car1.start()






######------Enapsulation-----######



class Person:
    def __init__(self, name):
        self.__name = name 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person("Nitish")
print(p.get_name()) 

p.set_name("Shradha")
print(p.get_name()) 
print()




######-----del keyworf----######


class Student:
    
    def __init__(self, name):
        self.name = name
student1= Student("Nitish kumar")

del student
print(student1)




####-----private(like) attributes & methods-----#####


class Account:
    def __init__(self, account_no, account_pass):
        self.account_no=account_no
        self.__account_pass=account_pass  # use "__ to the attribute to make is priavte in the class "

    def reset_pass(self):
        print(self.account_pass)

account1= Account(92834566 , 6439982983456 )
print(account1.account_no)
print(account1.reset_pass)

#one more example 

class CricketPlayer:
    def __init__(self, name):
        self.name = name         # Public attribute
        self.__runs = 0          # Private attribute

    def add_runs(self, score):
        self.__runs += score
        print(self.name, "scored", score, "runs.")

    def show_runs(self):
        print("Total runs by", self.name, ":", self.__runs)

    def __secret_message(self):  # Private method
        print("This is a private message for", self.name)

    def show_message(self):
        self.__secret_message()  # Call private method inside class

player = CricketPlayer("Nitish kumar")

player.add_runs(269)
player.show_runs()
player.show_message()

print()




#####--------INHERITANCE------#####


class Car:
    color="Black"
    @staticmethod
    def start():
        print("car started..")

    def stop():
        print("car stoped..") 

class Toyotacar(Car):
    def __init__(self, name):
        self.name=name


Car1=Toyotacar("Fortuner")
Car2=Toyotacar("Innova")

print("Car name is:",Car1.name, "\nCar colour is:", Car.color)
Car1.start()
print("And the", Car1.start())