#SECTION 2 - FUNCTIONS (20PTS TOTAL)

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function

length = str(input("Type anything: "))
a = 0
for i in range(len(length)):
    a += 1
print(a)

# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
side_length_one = int(input("Enter one side length of your triangle: "))
side_length_two = int(input("Enter another side length of your triangle: "))
hypotenuse = (side_length_one ** 2 + side_length_two ** 2)** 0.5
print(hypotenuse)

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)

# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
