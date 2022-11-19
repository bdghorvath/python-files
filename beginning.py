#basic plain text strings and how to print it
phrase = "Ben Horvath "

#simple "replace" function that allows for Ben (from above) to be replaced by Andrew
print(phrase.replace("Ben", "Andrew"))

#Do basic math without having to put quotation marks under the numbers and it will print out right for you
print(-0.5 + 5 )

#In order to convert a number to a string (text), you need to use the function "str"
number = 23
print (str(number ) + str(5) + " Hello!")

# Conversely, you need to use the function "int" to get a number (in string form) to convert it back to an integer string
# This can also work with decimals too but you need to use "float" as the function
example = "5.5"
print (float(example) + 5)

#abs function - absolute value
num = -5
print(abs(num))

#pow = power function (6^2 = 36)
print(pow(6,2)) # will output 36

#min/max function will tell us what the minimum/maximum value is between a range of different numbers

print(max(2,4,6)) # output is 6
print(min(2,4,6)) # output is 2

#round function will round a number like we usually do with math

print(round(5.5)) #will output 6

#now we will move over to importing certain libraries - enter beginningpt2.py -->
