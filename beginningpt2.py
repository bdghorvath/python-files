from math import * 
#expanding our math function capabilities
#has square root, pi, tau, infinity, etc. found here: https://www.geeksforgeeks.org/python-math-module/

#floor will always round down, "ceil" does the opposite, sqrt, well, you know that...
print (sqrt(36))
print (floor(3.6))
print (ceil(3.7))

#never be afraid to google "math functions in Python" - you never know what's out there until you try

#now, let's get some inputs...

name = input("Enter your name: ") #that's it, that's the function "input"
#just make sure that you have the variable and then ask for the input right there
age = input("Enter your age: ")

print("Hello " + name + ", how are you?\n I heard you are " + age + " years old.")

#Done with this, now moving on with a calculator --> calculator.py