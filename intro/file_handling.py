#!/usr/bin/python3

myFile = open("test.txt", "r") 

for line in myFile:
    print(line.upper())

myFile.close()