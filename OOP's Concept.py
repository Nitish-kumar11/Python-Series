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