'''def name():
    a = input("enter user name")
    print("hello",a)
  
name()'''
'''def sum():
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
     
    return a + b
print(sum())'''
'''def average():
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    c = int(input("enter third number : "))
    sum = a + b + c
    return(sum/3)


def square():
    a = int(input("enter a number : "))
    return a * a '''

#default arguments
'''def multiplication(a=5,b=3):
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
'''def check_even_odd():
    num = int(input("enter a number : "))
    if num % 2 == 0:
        return (num,"is even")
    else:
        return (num,"is odd")'''
'''def isgreater():
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    if a > b:
        return (a,"is greater than",b)
    elif a < b:
        return (b,"is greater than",a)
    else:
        return ("both numbers are equal")'''
'''
def ismax():
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))    
    c = int(input("enter third number : "))
    if a > b and a > c:
        return (a,"is the greatest number")
    elif b > a and b > c:
        return (b,"is the greatest number")
    elif c > a and c > b:
        return (c,"is the greatest number")
    else:
        return ("all numbers are equal")'''

'''def ispositive_negative():
    num = int(input("enter a number : "))
    if num > 0:
        return (num,"is positive")
    elif num < 0:
        return (num,"is negative")
    else:
        return ("the number is zero")'''
'''def sumofn():
    n = int(input("enter a number : "))
    sum = 0
    for i in range(1,n+1):
        sum += i
    return ("the sum of first",n,"natural numbers is",sum)
    '''
'''def factorial():
    n=int(input("enter any number"))
    fact=1
    for i in range(1,n+1,1):
        fact *=i
    return ("the factorial of",n,"is",fact)'''
'''def table():
    n = int(input("enter a number : "))
    for i in range(1,11):
        print(n,"x",i,"=",n*i)'''
'''def count_even():
    n = int(input("enter a number : "))
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            count += 1
    return ("the count of even numbers from 1 to " + str(n) + "is" + str(count)
'''


def  sum(*n):
    sum = 0
    for i in n:
        sum += i
    return("the sum of the numbers is",sum)
sum()