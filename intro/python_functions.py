#!/usr/bin/python3

def func1():
	print("This is a function")

func1()

#Functions can have arguments and can return values
def func2(name):
	return name

func2("security")

# Default arguments
def func3(age,name="security"):
    print(name, age)

# Positional arguments
def fruits(amount,*fruit):
    print(type(fruit))
    print("I like to eat {} {} everyday".format(amount,' and '.join([x for x in fruit])))

fruits(3,"apples","oranges","bananas")

# Keyword arguments
def cars(**kwargs):
    for key,value in kwargs.items():
        print(key , value)
    # for key in kwargs: 
    #     print(key, kwargs[key])

cars(German='BMW',French='Peugot')

# Variable scopes
def func4():
	global a
	a="test"
	print(a)

print(a)

# Functions calling other functions
def func5():
	a="This is function1"
	print(a)


def func6():
	func5()
	print("This is function2")

func6() 

# Recursion
def func7(a):
    print(a)
    if a > 0:
        function1(a-1)

func7(5)

