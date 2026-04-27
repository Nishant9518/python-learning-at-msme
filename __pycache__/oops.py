'''' creating of class and its instance'''
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def full_name(self): # ye humne ek funcionalty bnai h na ki object
             return f" {self.brand} {self.model}"
'''class ElectricCar(Car):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
        
    def full_name(self):
        return f"{super().full_name()} with a battery capacity of {self.battery_capacity} kWh"
My_tesla = ElectricCar("Tesla","Model S",100)
print(My_tesla.full_name())'''
    
car1 = Car("Toyota","Camry")
car2 = Car("Honda","Civic") 
print("Brand:",car1.brand)
print("Model:",car1.model)  
print("Brand:",car2.brand)
print("Model:",car2.model)
print(car1.full_name())
print(car2.full_name())