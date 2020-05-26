
friends = ["Kevin", "Mike", "John","Gimy","Garry"]
lucky_number = [1,7,9,11,10,5]

print(friends)

# Get Index of Element from lists
print(friends.index("Kevin"))

# We can Sort the list
#print(friends.sort())

# extend list
friends.extend(lucky_number)
print(friends)

# Append Element in list
friends.append("AppendElement")
print(friends)

# We can Insert Element in List
friends.insert(0,"InsertElement")
print(friends)

# Count the Element  the list
print(friends.count("Mike"))


