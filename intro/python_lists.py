#!/usr/bin/python3

list1 = ["A","B","C","D"]
print(list1)


# list1["A"] = "F"
# print(list1)

#Modifying items
list1[1] = "Z"
print(list1)

#Appending items
list1.append("E") 
print(list1)

#inserting items
list1.insert(2,"X")
print(list1)

#popping items
list1.pop()
print(list1)

# deleting items
del list1[2]
print(list1)

# list2 = "P" + list1
# print(list2)

# Combining lists
list2 = ["P"] + list1
print(list2)

#Max and min values
print(max(list1))
print(min(list1))

#Finding the index of an item
print(list1.index("Z"))

#reversing a list
list1.reverse()
print(list1)

list1 = list1[::-1]
print(list1)

# Counting
list1.append("Z")
print(list1.count("Z"))

# Extending lists
list3 = ["H","G","W"]
list1.extend(list3)
print(list1)

#Clearing a list
list1.clear()
print(list1)

# Sorting a list
list4 = [2,6,4,3,8,12,5]
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

# Copy a list
list5 = list4
print(list4)
print(list5)
# This is passing by reference and not copying
list4.append("Q")
print(list4)
print(list5)

# Use copy to do an actual copy
list6 = list4.copy()
list6.append("P")
print(list4)
print(list6)

# Map function

list7 = ["a","b","c"]
print(list7)

def uppercase(char):
    return char.upper()


list8 = list(map(uppercase,list7))
print(list8)

# Zip function

list9 = ["python","C", "C#", "java"]
list10 = [ 1,2,3,4]

for a, b in zip(list9,list10):
    print(f"{a} has number {b}")

print(list(zip(list9,list10)))
myDict = dict(zip(list9,list10))
print(myDict)