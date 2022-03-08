#user input from terminal

name = input("What is your name: ") #to input a number you need to cast it
age = int(input("How old are you: "))
height = float(input("How height are you:"))

age += 1

print("Hello "+name)
print("Next year you will be "+str(age))
print("You are "+str(height)+"cm tall")