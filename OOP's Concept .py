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
