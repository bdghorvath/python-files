#need to review and explain in detail about this try/except concept
while True: 
    try:
        num = int(input("enter number: "))
    except ValueError:
        print("you must enter an integer")
        continue
    else:
        break
print(num)

#complete!