#Check the type of input given

a=input("Enter a value to check its type: ")
print(type(a))

#It will always give string type because input function reads any value as string by default unless its mentioned with a specific datatype

# for example:

a=int(input("Enter a value:"))
print(type(a))

#This will give type as integer value, because its mentioned that the input should be given in int data type