# Create a program that will --

# Iterate the given list of numbers and print only those numbers which are divisible by 5.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Expected results

# Given list is [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

# Set of numbers given
setlist = [10, 20, 33, 46, 55]
print("The given list: ", setlist)

# Looking for the numbers that are divisible by 5
print("Numbers divisible by 5: ")
for numbers in setlist:
    if numbers % 5:
        print(numbers)