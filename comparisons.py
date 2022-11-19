# it doesn't matter where you put the print or the functions but I believe the proper way to do it is to set up the 
# functions above and then work your way down
def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("Enter the first number: ")
num1 = input()
print("Enter the second number: ")
num2 = input()
print("Enter the third number: ")
num3 = input()

print(maxnum(num1, num2, num3))