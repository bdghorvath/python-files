#previous - python functions
#return function will allow us to pull information from a given function (if statement= what was the result?)

def cubic(number):
    number * number * number

print(cubic (3)) #this will give us nothing if we don't have a return value

def cubic(number):
    return number * number * number
    print("this won't print") #why won't this print? because the return statement will cut everything off underneath it and continue moving forward

print(cubic (3)) #this will give us the proper number - WE NEED TO GET THE RETURN VALUE

result = cubic(5)
print(result) #this will give us 5^3 = 125

#next ifstatements.py