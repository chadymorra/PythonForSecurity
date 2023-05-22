#!/usr/bin/python3

# variables
a = "Python for "
b = 1
c = 1.1

print(type(a))
print(type(b))
print(type(c))

# Concatenation
d = "security"

e = a + d 

print(e)

# f = a + b

# print(f)

#print(help(print))

a , b = "Python 4 ", "fun"

print(a + b)


# Typecasting

a = "1"

b = int(a)

print(type(a))
print(type(b))

# Floats

grade = 9.1
print(type(grade))

final = int(grade) 
print(type(final))
exam = str(grade)
print(type(exam))

# Lists

cars = ["peugot", "bmw", "porsche", "mercedes"]

print(type(cars))

car1,car2,car3,car4 = cars

print(car1)
print(car2)
print(car3)
print(car4)

# Dictionaries

books = {"maths" : 1, "biology" : 2, "chemistry" : 3 }

print(type(books))

# Tuples

security = ("Python", "pentesting", "red team", "blue team")

print(type(security))

# Bool

student = True
teacher = False

print(type(student))
print(type(teacher))

# Range

ran = range(5)
print(type(ran))

# Byte

byte = b"something"

print(type(byte))


