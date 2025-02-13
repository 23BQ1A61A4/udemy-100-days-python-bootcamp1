# 1. if statement

height = int(input("Enter your height in cm: "))

if height > 120:
    print("You can ride the rollercoaster!")

# 2. if-else statement

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive yet.")

# 3. elif statement

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 4. Nested if statements

height = int(input("Enter your height in cm: "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# 5. Logical Operators

age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").lower()

if age >= 18 and has_license == "yes":
    print("You can drive.")
else:
    print("You cannot drive.")

# Another example:
if age < 18 or has_license == "no":
    print("You cannot drive.")
else:
    print("You can drive.")

# Using 'not':
is_student = True
if not is_student:  # If is_student is False
  print("Not a student")
else:
  print("Is a student")


# 6. Comparison Operators

print(10 > 5)   # True
print(10 < 5)   # False
print(10 >= 10)  # True
print(10 <= 5)   # False
print(10 == 10)  # True (equality check)
print(10 != 5)   # True (not equal)

# Example Project: Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
true_count = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
love_count = l + o + v + e

love_score = int(str(true_count) + str(love_count))

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your love score is {love_score}, you are alright together.")
else:
  print(f"Your love score is {love_score}.")