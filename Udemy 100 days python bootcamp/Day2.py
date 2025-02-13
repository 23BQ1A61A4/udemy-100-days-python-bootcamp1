# 1. Data Types (Review and Expansion)

# Integer
age = 30

# Float
height = 5.8

# String
name = "Angela"

# Boolean (True or False)
is_student = True

print(type(age))      # Output: <class 'int'>
print(type(height))   # Output: <class 'float'>
print(type(name))     # Output: <class 'str'>
print(type(is_student)) # Output: <class 'bool'>

# 2. Type Conversion (More Practice)

num_char = len(input("Enter your name: ")) # Input is always a string!
new_num_char = str(num_char) # Convert to string for concatenation

print("Your name contains " + new_num_char + " characters.")

# Converting to other types:
print(float("3.14159")) # String to float
print(int("123"))      # String to integer


# 3. Mathematical Operations

print(3 + 5)    # Addition
print(7 - 4)    # Subtraction
print(3 * 2)    # Multiplication
print(6 / 3)    # Division (always results in a float)
print(2 ** 3)   # Exponentiation (2 to the power of 3)
print(10 % 3)   # Modulo (remainder after division)
print(10 // 3)  # Floor Division (integer division)

# Order of Operations (PEMDAS/BODMAS): Parentheses, Exponents, Multiplication and Division (left-to-right), Addition and Subtraction (left-to-right)
print(3 * (3 + 3) / 3 - 3)  # Output: 3.0

# 4. Number Manipulation and Rounding

score = 0
score += 1 # Increment by 1
print(score) # Output: 1

score -= 1 # Decrement by 1
print(score) # Output: 0

score *= 2 # Multiply by 2
print(score) # Output: 0

score /= 2 # Divide by 2
print(score) # Output: 0.0

# Rounding
print(round(8 / 3, 2))  # Output: 2.67 (rounds to 2 decimal places)
print(round(8 / 3))     # Output: 3 (rounds to the nearest whole number)

# Floor division (always rounds down)
print(8 // 3) # Output: 2

# 5. f-Strings (Formatted String Literals)

score = 10
height = 1.8
isWinning = True

# Old way (using str() for type conversion):
print("Your score is " + str(score) + ", your height is " + str(height) + ", and you are winning is " + str(isWinning))

# f-strings (much cleaner and easier!):
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}")

# Example Project: Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill between? "))

tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / num_people

# Using f-strings for formatted output:
final_amount = "{:.2f}".format(bill_per_person) #Formats to 2 decimal places.
print(f"Each person should pay: ${final_amount}")