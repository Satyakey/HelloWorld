import random
print("Enter a value from 0 to 10: ")
number = int(input())
print("The number entered by you is ", number)
if(number > 10 or number < 0):
  print("Invalid Number!")
elif(number > 5):
  print("Number is above mid")
elif(number== 5):
  print("Number is mid")
else:
    print("Number is below mid")
  
print("Printing a random number", random.randint(1,11))

