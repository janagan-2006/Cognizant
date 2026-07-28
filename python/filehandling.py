f=open("summa.txt",'r+')
#data=f.read() # helps to read entire file at once
#data=f.readline() # helps to read one line at a time
data=f.readlines() # helps to read all lines at a time and give it as a list
print(data)
f.write("\n The sum of 5 and 10 is: 12")
f.close()

# in the above method you manually declare close function but following method 

# with open("summa.txt",'r') as f:
#     data=f.read() #     print(data) 