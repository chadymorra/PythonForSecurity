#!/usr/bin/python3

myTuple = ("item1","item2","item3")

# myTuple.append("item4")
# print(myTuple)

anotherTuple = ("item4","item5","item6")

# We can combine them but we cannot modify them
combTuple = myTuple + anotherTuple
print(combTuple)

item1, item2, item3 = myTuple
print(item1)
print(item2)
print(item3)

