#!/usr/bin/python3
# Strings
# myStringA = "Hello World"

# # Multiline strings
# myStringB = """Hello
# world!!!
# This is a
# multiline
# string"""
# print(myStringB)

## Multiplying strings
# myStringC = "this " * 10
# print(myStringC)


# myStringA = "Hello World"
# # Bool includes
# print("Hell" in myStringA)

# # Count of char in str
# print(myStringA.count("H"))

# # Find the length
# print(len(myStringA))

# #starts with
# print(myStringA.startswith("H"))

# #ends with
# print(myStringA.endswith("d"))

# # Find the index
# print(myStringA.index("Hello"))

# # uppercase
# print(myStringA.upper())

# #lowercase
# print(myStringA.lower())

# myStringD = "    This has spaces      "

# #Stripping spaces
# print(myStringD.strip())
# print(myStringD.rstrip())
# print(myStringD.lstrip())

# # Replacing stuff
# myStringE = myStringD.replace("spaces","tabs")
# print(myStringE.strip())


# myString = "Hello World"

# anotherString = myString.split(" ")
# print(anotherString)

# print(type(anotherString))

# myUrl = '<a href="https://example.com">Example</a>'

# url = myUrl[9:28]
# print(url)

# # Split url 1
# url = myUrl.split('"')
# print(url[1])

# # Split url 2
# start = "http"
# end = "\">"
# url = myUrl[myUrl.index(start):myUrl.index(end)]
# print(url)

#Join Url
# url = myUrl.split('"')
# newUrl = ('"').join(url)
# print(newUrl)



# String Formatting

myStringA = "this      "

print(f"{myStringA} is the Python for security course")
print("{} is the Python for security course".format(myStringA))
print("{myStringA} is the Python for security course".format(myStringA=myStringA.strip()))


myStringB = 45
print("{myStringB:x} is the Python for security course".format(myStringB=myStringB))
print("{myStringB:b} is the Python for security course".format(myStringB=myStringB))
print("{myStringB:o} is the Python for security course".format(myStringB=myStringB))




