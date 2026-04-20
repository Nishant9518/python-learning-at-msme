'''def name():
    a = input("enter user name")
    print("hello",a)
   
name()
def addition():
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    add = a + b
    print(add)
    
    
addition()
#default arguments
def multiplication(a=5,b=3):
    mul = a * b
    print(mul)
multiplication()
#variable length arguments
def addition(*numbers):
    sum = 0
    for i in numbers:

        sum += i 
        print(sum/len(numbers))
addition(5, 3, 2)
#required arguments
def name(fname,lname):
    print("hello",fname,lname)
name("Nishant","Bhardwaj")'''