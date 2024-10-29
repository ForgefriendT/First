#If I want the length of a string:

name="fauzan baig"
print(len(name))


#If I want to check if a string ends or starts with a specific letter or a few letters
#It will give output in True or False

print(name.endswith("zan")) #if I want to check ending of a string
print(name.startswith("Fau")) #if I want to check starting of a string


#If I want to capitalize the first letter of the string:

print(name.capitalize()) #This will only capitalize first word's first letter
print(name.title()) #This will capitalize first letter of each word


#Case changer

print(name.lower())
print(name.upper())


#Replace and Find

print(name.find("baig")) #Find index number of any word
print(name.replace("baig", "Engineer")) #Replace any word