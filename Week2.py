# Week 2 - 03/05

# 1. Write a python program to get a string from a given string where all occurrence of its first char have
# been changed to '$', except the first char itself! sample String : 'restart' Expected  -- result : 'resta$t'

string1 = "restart"
first_letter = string1[0]
length = len(string1)

for iterator in range(1,length):
     if first_letter == string1[iterator]:
         string1 = string1[0:iterator]+'$'+string1[iterator+1:length]

print(string1)

# 2. Write a python program to remove the nth index character from a nonempty string.
string1 = "restarthello"
index = int(input("Enter the index value:"))
string1 = string1[0:index]+string1[index+1:]
print(string1)

# 3. Write a python program to find the first repeated character in a given string.
string1 = "character"
length = len(string1)
for iterate in range(1,length):
    if string1[iterate] in string1[:iterate]:
        print("The first repeated letter: ",string1[iterate])
        break

# Week 2 - 05/05

# 4. Write a python program to find the second smallest number in a list.
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list1.remove(min(list1))
print(min(list1))

# 5. Write a python program to change the position of every nth value with the n+1 th in a list.

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
index1 = 5
for i in range(1, len(list1)):
    if i%index1 == 0:
        list1[i-1], list1 [i] = list1[i], list1 [i-1]
print(list1)

# Week 2 - 07/05

# 6. Write a python program to find a minimum value and maximum value in a set

# 7. Write a python program to convert a list of tuples of tuples into a  dictionary.
tup =[('Subbu' , 10), ('mahesh' , 25), ('dilli' , 30)]
print(dict(tup))
# or # print(dict([('Subbu' , 10), ('mahesh' , 25), ('dilli' , 30)]))

# 8. Write a python program to find the repeated items of a tuple.

# 9. for kid, name in cities.items():print(kid, name)
cities = {1 :"subbu" , 2 : "navven" , 3 : "murali"}
for kid,name in cities.items():
    print(kid,name)