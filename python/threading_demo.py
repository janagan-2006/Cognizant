import threading

# def task(nums):
#     print(f"Running...{nums}")

# t1 = threading.Thread(target=task(1))
# t2 = threading.Thread(target=task(2))
# t2.start()
# t1.start()

# class MyThread(threading.Thread):

#     def run(self):
#         print("Running")
#         self.nantha()
#     def nantha(self):
#         print("Hello")

# t = MyThread()

# t.start()  # it only execute the run method 

import threading

class BankAccount:

    def __init__(self):
        self.balance = 1000

    def withdraw(self, amount):
        self.balance -= amount

class WithdrawThread(threading.Thread):

    def __init__(self, account):
        super().__init__()
        self.account = account

    def run(self):
        self.account.withdraw(500)

account = BankAccount()

t1 = WithdrawThread(account)
t2 = WithdrawThread(account)

t1.start()
t2.start()

t1.join()
t2.join()

print(account.balance)  # output may be 0 or 500 depending on the thread execution order, demonstrating

# solution is locking 

