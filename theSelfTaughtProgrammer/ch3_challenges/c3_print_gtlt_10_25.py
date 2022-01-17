# Write a program that prints a message if a variable is less than or equal to 10,
# another message if the variable is greater than 10 but less than or equal to 25,
# and another message if the variable is greater than 25

x = 3

# case1: x <= 10
# case2: x >= 10 AND x <= 25
# case3: x > 25

if x > 25:
   print("The number is greater than 25")
elif x >= 10:
   print("The number is greater than or equal to 10 but less than 25")
else:
   print("The number is less than or equal to 10")
