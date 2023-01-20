class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print('This car is driving')
    
    def stop(self):
        print('this car has stopped')

car_1 = Car('Chevy', 'Corvette', 2021, 'blue')

print(car_1.drive())