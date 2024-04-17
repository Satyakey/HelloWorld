from StringMethods import strings, exclam

test = "test variable"
print("Hello World")
#Strings are Immutable
print(test[0:4])
print(strings + " " + strings.upper())
preReplace = (exclam.rstrip("?")).lstrip("?")
print(preReplace)
print(preReplace.replace("what","why"))
