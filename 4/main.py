#string method 

name ="Emanuele Micheletti"
print(len(name)) 
print(name.find("B")) # -1 if not found, index otherwise
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit()) #false if contains alpha char, True only if all chars are numeric
print(name.isalpha()) #space is not alpha
print(name.count("e"))
print(name.replace("e", "a"))
print(name*3)