'''a = {"apples": 5, "oranges": 3, "bananas": 2}
print(a["apples"])  # Output: 5
print(a["oranges"])  # Output: 3
print(a["bananas"])  # Output: 2'''


'''
employees = {
    "nishant": {"age": 21, "salary": 50000},
    "Khushi": {"age": 25, "salary": 60000},
    "rohit": {"age": 30, "salary": 70000}
}

highest_salary = 0
highest_paid_employee = ""

for name, details in employees.items():

    if details["salary"] > highest_salary:

        highest_salary = details["salary"]
        highest_paid_employee = name

print(f"Highest paid employee: {highest_paid_employee} (${highest_salary})")
print(employees.keys())
print(employees.values())
print(employees.items())'''
'''cart = []

def add_item(item_name, item_price):
    new_item = {"name": item_name, "price": item_price}
    cart.append(new_item)
    print(f"Added {item_name} to the cart.")


def calculate_total():
    total = 0
    for item in cart:

        total = total + item["price"]
    return total


def remove_item(name_to_remove):

    for item in cart:
        if item["name"] == name_to_remove:
            cart.remove(item)
            print(f"Removed {name_to_remove} from the cart.")
            return 


add_item("Milk", 50)
add_item("Bread", 30)
add_item("Chocolate", 100)

print(f"Total price: {calculate_total()}")

remove_item("Bread")

print(f"Final Total: {calculate_total()}")'''
'''sentence = "Nishant , Ram , Ram , yogesh,janvi,janvi, hardeep"

unique_words = set()
current_word = ""
for ch in sentence:
    if ch == " " or ch == ",":
        
        if current_word != "":
            unique_words.add(current_word)
            current_word = "" 
    else:
        
        current_word += ch


if current_word != "":
    unique_words.add(current_word)

print(f"Unique words: {unique_words}")'''
'''dict = {"a":3 , "b":2 , "c":4 }
b = sorted(dict.values())
print(b)'''
'''phonebook = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    
    phonebook[name] = number
    print(f"{name} added successfully!")
    
def search_contact():   
    name = input("Enter name to search: ")
    
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print("Contact not found!")'''


# words = sentence.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1


'''sentence = "python is great and python is easy to learn"
words=sentence.lower().split()
word_num={}



for word in words:
    if word in word_num:
        word_num[word]+=1
    else:
        word_num[word]=1
for k,v in word_num.items():
    if v==1:
        print(f"'{k}' unique") '''
    
        


    