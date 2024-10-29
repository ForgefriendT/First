a=(0,1,2,3,3,4,5,6,7)
print(a)


#a.count is used to count the number of times an element is entered inside a tuple
no=a.count(3)
print(no)


#a.index is used to return the value of index number that a specific element first occurs at
#for example I want to find where 3 occurs first
oc=a.index(3)
print(oc)


#Concatenation is used to add two tuples and make a new one
b=(10,20,30,40,50,60,70,100)
concatenation=a+b
print(concatenation)

#Repetition
repeated=a*3
print(repeated)

#Membership to check if an item exists inside a tuple
print(2 in a)
print(47 in a)
#Using "in"

#Length
len()