#maybe try pasting these into a Jupyter notebook because I think you can compartmentalize these different things
#Always make sure that you start coding on the second line bc apparently I fucked up the syntax???
numbers = [22, 23, 25, 39, 94, 34, 59]
friends = ["Ben", "Phil", "Alex", "Caleb", "Andrew", "Daoud"]

friends.extend(numbers) #extend will allow you to add two arrays together
print(friends)

friends.append("Kassen") #append will allow you to add a value to the end of the array
print(friends)

friends.insert(3, "Alan") #insert will put that value into that new position
print(friends)

friends.remove("Alan") #remove will just remove the given value
print(friends)

friends.clear #will get rid of the entire list
friends = ["Ben", "Phil", "Alex", "Caleb", "Andrew", "Daoud"] #just repopulating it for other functions below

friends.pop() #will remove the last item off of the list
print(friends)

print(friends.index("Ben")) #will tell you the position of the value in the array
print(friends.index("Andrew")) #will tell you the position of the value in the array
#print(friends.index("Kelly")) #if not in the array, there will be an error saying that they are not in the list
 #remove the # if you want to see the error, if not, we will move on.

friends = ["Ben", "Ben", "Phil", "Alex", "Caleb", "Andrew", "Daoud"]
print(friends.count("Ben")) #will just display how many "Bens" are in the list

friends.sort() 
# need to make sure we always put the () in front of that function if it is not specifically targeting something because it will be a dead function
# this will make it a dead 
print(friends)

friends.reverse() #this will just make the order reversed
print(friends)

friends2 = friends.copy #this will make a copy of a given array
print(friends)