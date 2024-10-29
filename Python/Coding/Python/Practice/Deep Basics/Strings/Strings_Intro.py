#POSITIVE SLICING OF A STRING

name = "Fauzan"

print("There are", len(name),"characters")

nameshort=name[0:4] #Start from index 0 all the way till 3 (Excluding 3)

print(nameshort)

#NEGATIVE SLICING OF A STRING

print(name[-4: -1])

#If there is nothing before the collen then it means string should start from 0 index

print(name[:5])

#If there is nothing after the collen then it means string should end at the last index

print(name[0:])

#If I want to skip a few index in between I can use name[start:end:"number of indexes to skip"]

print(name[0:6:4])
print(name[1:5:3])