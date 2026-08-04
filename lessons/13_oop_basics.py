#OOP_basics
class Car:
    total_cars_created = 0
    def __init__(self, make, model, year, mileage = 0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        Car.total_cars_created +=1
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    def drive(self, miles):
        self.mileage = miles + self.mileage
        print(f"Drove {miles} miles. Total mileage: {self.mileage}") 
        return self.mileage
    def info(self):
        print(f"{self.year} {self.make} {self.model} - {self.mileage} miles")
class SportCar(Car):
    def __init__(self, make, model, year, top_speed, mileage=0,):
        super().__init__(make, model, year, mileage)
        self.top_speed = top_speed
    def boost(self):
        print(f"Zooming at {self.top_speed} mph!")
c1 = Car("Toyota", "Corolla", 2020)
c2 = Car("Honda", "Accord", 2022)
sc1 = SportCar("Ferrarri", "spyder", 2024, 340)
print(c2)
c1.info()
c1.drive(60)
c1.info()
sc1.boost()
print(Car.total_cars_created)
