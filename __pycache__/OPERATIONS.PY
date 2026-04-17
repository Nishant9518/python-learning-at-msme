#a = [1,2,3,4]
#a.remove(3)
#print(a)
#a.insert(1,20)
#a.extend([5,6,7])
#print(a[0:3:1])b1  
#a =[]
#for i in range(3):
 #   a.append(int(input("enter number : ")))
#print(a)
#a = [1,2,3,4]
#a = [1,2,3,4]
#a.insert(2,20)
#print(a)
#b = [5,6,7]
#a.extend(b)
#print(a)
#a = [1,2,3,4]
#a.insert(0,6)
#print(a)
#a = a + [5,6,7]
#print(a)
#a = [7,8,9,4,67,43,87,34,23,45,2,67,43]
#b = set(a)
#print(b)
#b = list(b)
#b.sort()
#print(b)
#a = []
#for i in range(0,5):
 #   a.append( i)
#print(a)
#a = [ 55, 55,45,34,34,23,23,66,66]
#b = []
#for i in a:
  #  if i not in b:
 #       b.append(i)
#print(b)
#numbers = []

#for i in range(5):
 #   num = int(input(f"Enter number {i+1}: "))
  #  numbers.append(num)

#total = sum(numbers)
#average = total / len(numbers)
#maximum = max(numbers)

#print("List:", numbers)
#print("Sum:", total)
#print("Average:", average)
#print("Maximum:", maximum)

#a = input("Enter a string: ")
#vowels = "aeiouAEIOU"
#count = 0

#for i in a:
 #   if i in vowels:
  #      count += 1

#print("Number of vowels:", count)
a = [1,2,3,4,5,]
reverse = ""
for i in a :
    reverse = str(i) + " " + reverse
    
print(reverse)
b = [1,2,3,4,5]
print(b[::-1])
c = [1,2,3,4,5]
print(c[-1:4:-1])
