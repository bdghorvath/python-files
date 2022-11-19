
import math

operation = input("Enter in a value:\nB- Binary\nU- Unary\nV- Variable\nA- Operation with a variable(V)\nX- Exit\n")
operation = operation.upper()
#getting rid of the first if statement by just putting the upper operation and avoiding checking to see if it's a lower case 
    #update: it worked.

#if operation == ("b" or "u" or "v" or "a" or "x"):
    #operation = operation.upper() # operation variable needs to reclassify itself once we have the upper case function being run
#elif operation != ("B" or "U" or "V" or "A" or "X"):
while(operation) != ("B" or "U" or "V" or "A" or "X"):
    operation = input("Invalid input...\nEnter in a value:\nB- Binary\nU- Unary\nV- Variable\nA- Operation with a variable(V)\nX- Exit\n")

print(operation) #just testing to see what the output was

if operation == ("B"):
    binoperation = input("Enter in an operator: ") #what is WE DOIN'

#checking to see if I even need that if/elif statements
    if binoperation == ("+" or "-" or "*" or "/" or "%"): #missed the initial input check...
        while True: #why will the underneath become unactivated if the boolean is false? --> doesn't fulfill the while loop I suppose.
            try:
                num1 = float(input("Enter the first number: "))
            except ValueError: 
                #we must put ValueError in order to fulfill this logic 
                #ValueError documentation 1: https://en.wikipedia.org/wiki/Data_type
                #ValueError documentation 2: https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples 
                print("you must enter a valid entry for your first number")
                continue

            else:
                break

        print(num1)

        while True: 
            try:
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("you must enter a valid entry for your second number")
                continue
            else:
                break
        print(num2)
        print(binoperation)
            #need to determine that the input variable is going to be a number
                #get input & use the float.input function to turn it into a number
                #while invalid
                    #get input
    elif binoperation != ("+" or "-" or "*" or "/" or "%"):
        binoperation = input("Enter in an operator: ayo")
        while binoperation != ("+" or "-" or "*" or "/" or "%"):
            binoperation = input("Enter in an operator: bruh")
    print(binoperation)
    

elif operation ==("U"):
    print("still needs work")