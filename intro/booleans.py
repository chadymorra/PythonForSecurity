#!/usr/bin/python3


correct = True
incorrect = False

print(correct) 
print(incorrect) 


print(correct == True)
print(incorrect == True)

print("==========")
print(correct != True)
print(incorrect != True)

print("==========")



myStringA = ""

if myStringA: # if myStringA contains something
    print("True")
else:
    print("False")

print("==========")

if not myStringA: # if myStringA is empty
    print("True")
else:
    print("False")

print("==========")
myStringA = ""
myStringB = ""

if myStringA and myStringB: #if myStringA and myStringB are not empty
    print("True")
else:
    print("False")
print("==========")

if myStringA or myStringB: #if myStringA or myStringB are not empty
    print("True")
else:
    print("False")    