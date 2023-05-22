#!/usr/bin/python3


a = 10
b = "a"
print(hex(a))
print(bin(a))

# String to hex?
# print(hex(b))


print(ord(b))
print(hex(ord(b)))

#print(help(ord))
#print(help(ascii))

c = "this"


#print(ord(c))
print("===================")
ans = []
for char in c:
	#ans += hex(ord(char))
	ans.append(hex(ord(char))) 
print(ans)

# Hex to string?
myString = "\x46\x47\x65\x77"
print(myString)

