# 1. Printing to the console

print("Hello, World!")  # Prints "Hello, World!" to the console
print("My name is [Your Name].") # Replace [Your Name] with your actual name.
print(123) # Prints the integer 123
print(3.14159) # Prints a floating-point number

# 2. String manipulation

print("Hello" + " " + "World!") # String concatenation (joining strings)
print("Hello\nWorld!") # Newline character (\n) creates a line break
print("Hello\tWorld!") # Tab character (\t) adds a tab space

# 3. Variables

name = "Angela" # Assigning the string "Angela" to the variable 'name'
age = 30       # Assigning the integer 30 to the variable 'age'
height = 5.8   # Assigning a float to the variable 'height'

print(name)  # Prints the value stored in the 'name' variable
print(age)   # Prints the value stored in the 'age' variable
print(height) # Prints the value stored in the 'height' variable

# Example combining variables and strings:
print("My name is " + name + " and I am " + str(age) + " years old.") # Note the str() function to convert age to a string.

# 4. Input from the user

user_name = input("What is your name? ")  # Prompts the user to enter their name, and stores it in user_name.
print("Hello, " + user_name + "!")

# Example with type conversion:
age_str = input("What is your age? ")  # Input is always a string.
age = int(age_str) # Converts the string age to an integer.

print("You will be " + str(age + 1) + " years old next year.") # Calculating and displaying the next year's age.

# 5. Band Name Generator (A simple project often introduced on Day 1)

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)