a = int(input("enter first number : "))
op = input("enter operator : +, -, *, / :   ")
b = int(input("enter second number : "))
if op == "+" :
    print(a, "+", b, "=", a + b)
elif op == "-" :
    print(a, "-", b, "=", a - b)
elif op == "*" :
    print(a, "*", b, "=", a * b)    
elif op == "/" :
    if b != 0 :
        print(a, "/", b, "=", a / b)
    else :
        print("division by zero is not allowed")