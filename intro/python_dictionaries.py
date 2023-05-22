#!/usr/bin/python3

# Create key value pairs

myDict = {"a":1,"b":2,"c":3}

print(myDict)

#we can search by keys but not indexes
print(myDict["b"])

print(myDict.keys())
print(myDict.values())

print(myDict.items())

# Add new items

myDict["d"] = 4
print(myDict)

myDict["a"] = 0
print(myDict)

myDict.update({"a":3})
print(myDict)

myDict.pop("d")
print(myDict)

del myDict["b"]
print(myDict)

myDict['c'] = {"e":5,"f":6}
print(myDict)

print(myDict["c"]["e"])