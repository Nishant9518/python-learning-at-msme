class A:
    def __init__(self,car,model):
        self.brand = car
        self.model = model
class B(A):
    def __init__(self,car,model,year):
        super().__init__(car,model)
        self.year = year
class C(B,A):
    def __init__(self,car,model,year,color):
        super().__init__(car,model,year)
        self.color = color
print(C("BMW","X5",2020,"Black").__dict__)