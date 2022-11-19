#experiment with the booleans with both the male and tall variables
is_male = False 
tall = False

if is_male and tall: #syntax for if/else statements, if you want more cases, you must put OR or AND, or AND NOT - depending on the relationship
    print("You are a tall male")
    #again, with the or logic, if is_male or tall booleans are true, that print statement will carry through

elif is_male and not (tall): #tall = false to print this
    print("You are a male, but you are not tall")

elif (is_male) and not tall: #is_male needs to be false to print this condition
    print("You are a male, but you are not tall") #whatever variable you put under the case where it does not fulfill the AND NOT, then you can go thru

else:
    print("You are neither a male or tall")

#now onto comparisons.py