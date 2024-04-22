from StringMethods import *

test = "test variable1"
test2 = "AB123"
#Strings are Immutable
print(test[0:4])
print(strings + " " + strings.upper())
preReplace = (exclam.rstrip("?")).lstrip("?")
print(preReplace.center(20))
print(preReplace.replace("what", "why"))
print(exclam.split("?"))
print(test.find("var"))
print(" ".isspace())

if(test.isalnum()) : 
  print("Test is alphanumric")
else:
  print("Test isn't alphanumric")
  print("okay")

data = input("Enter a number: ")
print(data)