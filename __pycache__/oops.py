'''' creating of class and its instance
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
car1 = Car("Toyota","Camry")
car2 = Car("Honda","Civic")
print("Brand:",car1.brand)
print("Model:",car1.model)
print("Brand:",car2.brand)
print("Model:",car2.model)'''