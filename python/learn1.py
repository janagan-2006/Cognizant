# Python
name = "Alice"
age = 30
print("Name:",name, ", Age:", age) # Auto-adds spaces between arguments
product = "Laptop"
price = 999
quantity = 5  # Integer value
print(f"Product: {product} | Price: ${price:.3f} | Qty: {quantity}") # main
user = {"name": "Alex", "role": "Dev"}
print(user.get("age", 25))   # Outputs: 25 (Fallback value used since 'age' key doesn't exist)
print(list(user.keys()))
print(tuple(user.keys()))    
s=user.items()
print(s)       # dict_keys(['name', 'role'])
unique_numbers = {10, 20, 30,30}

for num in unique_numbers:
    print(num)
shopping_cart = []  # it is not meant None , it is empty.
if not shopping_cart:  # I am checking it is empty -> isEmpty()
    print("ok")
# Java-style: if (shoppingCart.isEmpty())
# # Pythonic style: Check if the collection itself is empty or full directly
# if shopping_cart is null:
#     print("Your cart is empty!")
print(5^3)  # xor operator
# in the string concept python and java both are same

original_str = "Java"
abs=original_str
# Attempting to change a character directly throws a TypeError:
# original_str[0] = "K"  #  ERROR! Python completely forbids this.

# Reassigning the variable:
original_str = original_str + " to Python"
print(original_str)
print(abs)

msg = "  Hello Python World  "
d=msg.replace(" ","")
print(d)
print(msg.strip().lower())  # Outputs: "hello python world" (Chaining works!)
print(msg.split()) # return as list 
x, y, z = 1, 2, 3

# # Swapping values (No temporary variable needed!)
# a = 10
# b = 20

# a, b = b, a
print("------------------------")

# list
x = [1, 2, 3]
y = x  # Both 'x' and 'y' now point to the EXACT SAME list object in memory!
z=[1,2,3]
if x == z: # it checks the value 
    print(True)
if x is not z: # it checks the memory address
    print(True)
y.append(4)
x.append(5)
print(y)  # Outputs: [1, 2, 3, 4,5]
words_list = ["Python", "is", "incredibly", "fast"]
result="".join(words_list) # list to string
a="charles"
b="charles1"
if a is b: #same string take same memory location like java
    print(" ama da") # true
a="char les"
b="char les"
print(a is b,"lksdf")  # false because string contains space even though same
# e = "hello-world"
# f = "hello-world"
# print(e is f)  # False (Separate memory addresses!)

# - It can **only** contain alphanumeric characters and underscores (`A-Z`, `a-z`, `0-9`, and `_`).
# - It **cannot** contain spaces, hyphens, or any other punctuation marks (`!`, `@`, `#`, `.`, etc.).

colors = ("cherry", "apple", "banana")
sortcolor=sorted(colors)  # Outputs: ['apple', 'banana', 'cherry']
# A completely locked, unchangeable set
locked_set = frozenset([1, 2, 3])
print(type(locked_set)) #<class 'frozenset'>
# locked_set.add(4)  # ❌ ERROR! AttributeError: 'frozenset' object has no attribute 'add'
# tuple allowed functions
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2)) 
my_tuple = ('a', 'b', 'c', 'b')
print(my_tuple.index('b'))  # Output: 1
print(len((10, 20, 30)))  # Output: 3
print(max((5, 12, 3)))  # Output: 12
print(sum((1, 2, 3)))  # Output: 6
print(sorted((3, 1, 2)))  # Output: [1, 2, 3]
print(tuple([1, 2]))  # Output: (1, 2)
# Packing values into a single variable
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

user_info = ["John", "Doe"]
greet(*user_info)  # Unpacks the list into the two required arguments

# Output: Hello, John Doe!
my_tuple = 1, 2, 3

print(my_tuple)  # Output: (1, 2, 3)
print(type(my_tuple))  # Output: <class 'tuple'>
a = 5
b = a  # Both point to the object '5'

a = a + 1  # 'a' now points to a new object '6'. 'b' still points to '5'!
print(b)   # Outputs: 5
# You might have a question like why list change if I change the initializer Why integer not change up because Python is an interpreter but list store in the memory location

# x=5
# print(x)
# x="lkfls"
# print(x)  # working fine

class ParentB:
    def log_message(self):
        print("Step 2: Parent B logs the data.")

class ParentA(ParentB):
    def log_message(self):
        print("Step 1: Parent A processes the data.")


# MRO Chain Order: Child -> ParentA -> ParentB
class Child(ParentA):
    def log_message(self):
        print("Step 0: Child initializes log.")
        super().log_message()
       # super().super().log_message()  # throw error
     #  If you want to access parent B class method then use like following
        super(ParentA,self).log_message() # it is check above parent any there or not otherwise it will throw error
        # above method only works when you inherit else throw
        # else you can use
        ParentB.log_message(self) # only if the class is public

obj = Child()
obj.log_message()

from abc import ABC, abstractmethod

# To make a class abstract, it must inherit from ABC
class Database(ABC):
    
    @abstractmethod
    def connect(self):
        pass  # Abstract methods have no body, just 'pass'

class MySQL(Database): # you must use the fucntions inside the adstract class else error
        def connect(self):
            print("Connected to MySQL!")

# db = Database() # ❌ ERROR! Python blocks instantiation of abstract classes like java.
db = MySQL()      # Works perfectly

class A:
    def __init__(self):
        print("A constructor")

class B(A):
    pass

class C(B):
    pass

c = C()  # A constructor
# from collections import deque

# # Initialize a fast queue container
# queue = deque()

# # ENQUEUE: Adding elements to the back of the line
# queue.append("Customer A")
# queue.append("Customer B")
# queue.append("Customer C")

# # DEQUEUE: Removing elements from the front of the line (First In, First Out)
# first_served = queue.popleft() 
# print(f"Served: {first_served}")  # Outputs: Customer A
# print(queue)   

# stack = []

# # PUSH: Adding elements to the top
# stack.append("Page 1")
# stack.append("Page 2")
# stack.append("Page 3")

# print(stack)  # Outputs: ['Page 1', 'Page 2', 'Page 3']

# # POP: Removing the top element (Last In, First Out)
# removed_item = stack.pop()
# print(f"Popped item: {removed_item}")  # Outputs: Page 3
# print(stack)  # Outputs: ['Page 1', 'Page 2']                   # Outputs: deque(['Customer B', 'Customer C'])


# class Node:
#     def __init__(self, data):
#         self.data = data      # Storing the value
#         self.next = None      # Storing the pointer reference to the NEXT node

# class LinkedList:
#     def __init__(self):
#         self.head = None      # The entry point pointer of the list

#     def append(self, data):
#         new_node = Node(data)
#         print(new_node)
#         if not self.head:
#             self.head = new_node
#             return
        
#         # Traverse down the references until we find the tail end
#         current = self.head
#         while current.next != None:
#             current = current.next
#         current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Usage
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.display()  # Outputs: 10 -> 20 -> 30 -> None


# *summa is called Arbitrary Positional Arguments
# **additional_info is called Arbitrary Keyword Arguments
def save_user_profile(username, *summa,**additional_info):
    print(type(username))
    print(type(additional_info))
    print(type(summa))
    print(f"Username: {username}")
    print(f"summa: {summa}")
    print(f"Other Data: {additional_info}") # This is a standard dictionary!
save_user_profile("12", 27,28,"klsd", city="Chennai", role="Developer")
z=(1) # integer
print(type(z)) 
print(z)
z=(1,2) # tuple
print(type(z))
print(z)
z=(1,)
print(z) # tuple
nums = (1,2,3)
a= [[1,2], [3,4]]

b=a.copy()
b.append(3)
b[0].append(99)

print(a)
print(b)
result = map(lambda x: x%2==0, nums)
result2=filter(lambda x: x%2==0, nums)
# Here we can't directly use the list instead of map because List is only used for it data type like list tuple range So only use the map or filter
#In this statement we can use filter instead of but we get the output only true So that is the purpose of filter
print(list(result)) # output [False, True, False]
print(list(result2)) # output [2]

#Use a List Comprehension (Pythonic & Faster)
nums = [1, 2, 3]
result = [x for x in nums if x % 2 == 0]
print(result)


a, b = map(int, input().split(','))
print(f"{a}{b}")

count = 10

def increment():

    global count

    count += 1

increment()

print(count)

def outer():

    count = 10

    def inner():

        nonlocal count

        count += 1

        print(count)

    inner()

outer()

count = 100

def outer():

    count = 10

    def inner():

        nonlocal count

        count += 1

        print("Inner:", count)

    inner()

    print("Outer:", count)

outer()

print("Global:", count)