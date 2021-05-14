# Week 3 - 10/05

# 1. Write a python program to merge two python dictionaries.

dict1 = {'subbu': "Verginia", 'Naveen': "New York", 'Murali': "Mexico"}
cities = {1:"Subbu", 2:"Naveen", 3:"Murali", 4:"Subbu son1", 5:"Subbu son2", 6: "Subbu soninfi"}
dict1.update(cities)
print(dict1)

# 2. Write a python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)

# 3. Write a python program to get next day of given date using if-elif-else.

date = "03/11/1991"
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])
print(type(day),day)
print(type(month),month)
print(type(year),year)

week = (day+ 2*month +3*(month+1)//5 + year + year//4 - year//100 + year//400 +2) %7

print("Week: ", week)

if (week == 0):
    print("Sunday")
elif(week == 1):
    print("Monday")
elif(week == 2):
    print("Tuesday")
elif(week == 3):
    print("Wednesday")
elif(week == 4):
    print("Thursday")
elif(week == 5):
    print("Friday")
else:
    print("Saturday")

#  4. Write a python program to check if the input number is - real number - float number - string - complex num - zero(0)

input_data = 'sdf'

print(type(input_data))
if(type(input_data) == type(" ")):
    print("data is string")
elif(type(input_data) == type(3)):
    print("data is an real number")
    if(input_data == 0):
        print("Data is Zero")
elif(type(input_data) == type(3.3)):
    print("data is a float")
    print("data is a real number")
elif(type(input_data) == type(3+5j)):
    print("data is a complex")
else:
    print("Unknown")

# 5. write a python program to check the user enters "lol", print("laughing out loud". if the user
# enters "rof1",print"rolling on the floor laughing". if the user enters "lmk", print "shaking my head".

str1 = input("user enter the word : ")

if str1 == "lol":
    print("laughing out loud")
elif str1 == "rof1":
    print("rolling on the floor laughing")
elif str1  == "lmk":
    print("shaking my head")
else:
    print("user enter the worng word")

# 6. Write a python program that asks a user how many pizza slices they want.The pizzeria
# charges Rs-123.00 a slice if user order even number of slices, price per slice is Rs-120
# print the total price depending on how many slices user orders.

slices = int(input("Enter the number of slices: "))

if(slices%2==0):
    print("Total cost: ", slices*123)
else:
    print("Total cost: ", slices*120)