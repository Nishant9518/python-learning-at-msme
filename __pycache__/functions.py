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

'''def  sum(*n):
    sum = 0
    for i in n:
        sum += i
    return("the sum of the numbers is",sum)
sum(1,2,3,4,5,6,7,8)'''

'''def highest_number(*n):
    highest_number=0
    for i in n:
        if i > highest_number:
            highest_number = i
    return (highest_number)
print(highest_number(1,34,56,24))'''

'''def student_info(*a, **j):
    for in a :
        print(i)
    for k,o in j.items():
        print(k,o)
        student_info("math","english", name= "nishant" , class = "btech")'''
 
'''
def analyze_number(*list ):
    even_count = 0
    odd_count = 0
    largest = list[0]
    smallest = list[0]

    
    for i in list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if i > largest:
            largest = i
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i

    return ("the count of even numbers is", even_count, "and the count of odd numbers is", odd_count, "the largest number is", largest, "the smallest number is", smallest)
print(analyze_number(1,2,3,4,5,6,7,8))'''
def password():
        passwrd = input("enter a password : ")
        upr =  False
        num = False
        lwr = False
        if len(passwrd) >= 8:
           for i in passwrd:
            if i.isupper():
                upr = True
            elif i.islower():
                lwr = True
            elif i.isdigit():
                num = True
                if(upr and lwr and num):
                    print("the password is valid")
                else:
                    print("the password is invalid")
password()

 

#name = input("enter your name : ")   
 