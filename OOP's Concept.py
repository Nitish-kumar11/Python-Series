class car:
   
    def __init__(self, fullname):
        self.brand= fullname
        print("adding new car..")
car1= car("BMW")
print(car1.brand)