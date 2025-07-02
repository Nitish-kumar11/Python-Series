###### CONSTRUCTOR IN PYTHON 

class car:
     #default constructor
     def __init__(self):
        pass
    
    #this is parametrized constructor
     def __init__(self, name, price ):
        self.brand= name
        self.price= price
        print("adding new car..")
car1= car("BMW", "2.5CR")
print(car1.brand, car1.price)

car2= car("Audi", "2.7CR")
print(car2.brand, car2.price) 


######  class attributes 

class car:
    made_in = "India"

    # this is a parametrized constructor
    def __init__(self, name, price):
        self.brand = name
        self.price = price
        print("adding new car..")

car1 = car("BMW", "2.5CR")
print(car1.brand, car1.price)
print(car1.made_in)

car2 = car("Audi", "2.7CR")
print(car2.brand, car2.price)




###### ONE MORE CLASS ATTRIBUTE EXAMPLE 

class student:
    college_name="Cambridge institute of technology"
    name="anonymous" #class attribute 

    def __init__(self, name , marks):
        self.name=name #object attribute 
        self.marks=marks

S1=student("Nitish kumar", 81) 
print(S1.name, S1.marks) # here name does't print anonymous because object attribute precedence is always high than class attribute 