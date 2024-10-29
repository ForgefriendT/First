friends=["Apple","Orange",5,345.06,False,"Chaitanya","Tanushree"]
print(friends)

#To add something at the end of the list, in this case Fauzan.
friends.append("Fauzan")
print(friends)


#To sort the list (only for numbers)
numbers=[1,35,23,2,567,234,578,683]
numbers.sort() 
print(numbers)


#To print the list starting from the last element
friends.reverse()
print(friends)


#To add elements in between the list we can use friends.insert(index number, value)
friends.insert(3,"I love coding")
print(friends)


#To delete element at a particular index use pop
friends.pop(5)
print(friends)

#To delete a specific element from the list
friends.remove(5)
print(friends)


