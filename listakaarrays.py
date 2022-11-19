
friends = ["Ben", "Phil", "Alex", 9]
print(friends[0])

#printing negative numbers prints the items at the back of the list
# -1 will print the last item
print(friends[-2]) #output Alex - because the 9 is there

morefriends = ["Ben", "Phil", "Alex", "Caleb", "Andrew", "Daoud"]

print(morefriends[1:]) #will print Phil all the way to Daoud
print(morefriends[1:3]) #will print Phil to Alex only - doesn't count the number that you're ending on - 
#technically start with that first number and then finish on the entry before 3.
# : allows us to give a range of items we want from that array

#modifying values = just put a new line below and run another program
print(morefriends)
morefriends[1] = ("Cockroach")
print(morefriends)


#next is list functions