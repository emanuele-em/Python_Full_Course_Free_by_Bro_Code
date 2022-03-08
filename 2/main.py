first_name = "Emanuele"
last_name = "Micheletti"
full_name = first_name + " " +last_name
print("Hello "+full_name)
print(type(full_name)) #print the type of a variable

age = 21
#age = age + 1
age += 1
print("Your age is "+str(age)) #casting from a type to another (in this case from int to string)
print(type(age))

height = 250.5 #american notation
print("Your height is "+str(height))
print(type(height))

human = False #only true or false
print("Are you a human: "+str(human))
print(type(human))