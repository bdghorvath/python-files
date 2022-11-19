
coordinates = (4, 5) #tuple is immutable - cannot be changed or modified - tuples are expressed with a parentheses
print(coordinates[0])

#coordinates[1] = 10 #this will create an error saying that 'tuple' object does not support item assignment
print(coordinates[:]) #need to put a colon in the middle in order to print everything in the tuple

#use tuples when you want to have values that you don't want to change at all- coordinates, actual given facts
#you can have tuples in lists, but not lists in tuples

coordinateslist = [(5,5), (4,5), (0,3), (8,5)] #this is possible, but you are going to have an array of just a couple of tuples
tuplecoordinate = ([3, 4, 5]) #this is the exact same thing as a regular tuple but the [] just makes it more sophisticated

print (tuplecoordinate[0])