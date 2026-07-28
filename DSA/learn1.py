# # Python
# name = "Alice"
# age = 30
# print("Name:",name, ", Age:", age) # Auto-adds spaces between arguments
# product = "Laptop"
# price = 999
# quantity = 5  # Integer value

# # Standard printing of an integer
# print("Price %.2f Quantity %d"%(price,quantity))
# print("{} dfska{}",100,100)
# print(f"Product: {product} | Price: ${price:.3f} | Qty: {quantity}")
user = {"name": "Alex", "role": "Dev"}
print(user.get("age", 25))   # Outputs: 25 (Fallback value used since 'age' key doesn't exist)
print(tuple(user.keys()))    
s=user.items()
print(s)       # dict_keys(['name', 'role'])
# unique_numbers = {10, 20, 30}

# for num in unique_numbers:
#     print(num)
# shopping_cart = []

# # Java-style: if (shoppingCart.isEmpty())
# # # Pythonic style: Check if the collection itself is empty or full directly
# # if shopping_cart is null:
# #     print("Your cart is empty!")

# print(5^3)
# original_str = "Java"
# abs=original_str
# # Attempting to change a character directly throws a TypeError:
# # original_str[0] = "K"  #  ERROR! Python completely forbids this.

# # Reassigning the variable:
# original_str = original_str + " to Python"
# print(original_str)
# print(abs)

# msg = "  Hello Python World  "

# print(msg.strip().lower())  # Outputs: "hello python world" (Chaining works!)
# print(msg.split())
# x, y, z = 1, 2, 3

# # Swapping values (No temporary variable needed!)
# a = 10
# b = 20

# a, b = b, a

# print("a: %d, b: %d"%(a,b))
# x = [1, 2, 3]
# y = x  # Both 'x' and 'y' now point to the EXACT SAME list object in memory!
# y.append(4)
# x.append(5)
# print(y)  # Outputs: [1, 2, 3, 4]
# a = 5
# b = a  # Both point to the object '5'

# a = a + 1  # 'a' now points to a new object '6'. 'b' still points to '5'!
# print(b)   # Outputs: 5

# x=5
# print(x)
# x="lkfls"
# print(x)

# class ParentB:
#     def log_message(self):
#         print("Step 2: Parent B logs the data.")

# class ParentA(ParentB):
#     def log_message(self):
#         print("Step 1: Parent A processes the data.")


# # MRO Chain Order: Child -> ParentA -> ParentB
# class Child(ParentA):
#     def log_message(self):
#         print("Step 0: Child initializes log.")
#         super().log_message()

# obj = Child()
# obj.log_message()

# from abc import ABC, abstractmethod

# # To make a class abstract, it must inherit from ABC
# class Database(ABC):
    
#     @abstractmethod
#     def connect(self):
#         pass  # Abstract methods have no body, just 'pass'

# class MySQL(Database):
#     def connect(self):
#         print("Connected to MySQL!")

# # db = Database() # ❌ ERROR! Python blocks instantiation of abstract classes.
# db = MySQL()      # Works perfectly

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

# def save_user_profile(username, *summa,**additional_info):
#     print(type(username))
#     print(type(additional_info))
#     print(type(summa))
#     print(f"Username: {username}")
#     print(f"summa: {summa}")
#     print(f"Other Data: {additional_info}") # This is a standard dictionary!
# z=(1)
# print(type(z))
# print(z)
# z=(1,2)
# print(type(z))
# print(z)

# nums = [1,2,3]

# result = map(lambda x: x%2==0, nums)
# print(list(result))
# a, b = map(int, input().split())
# print(f"{a}{b}")
# print(list(result))
# # We can pass any random named arguments we want!
# save_user_profile("12", 27,28,"klsd", city="Chennai", role="Developer")

def greet():
    print("Hello")
greet()

chars = list(input().split(' '))

print(chars)