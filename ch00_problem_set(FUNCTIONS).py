#SECTION 2 - FUNCTIONS (20PTS TOTAL)

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function

def length(ya):
    a = 0
    for i in range(len(ya)):
        a += 1
    print(a)
length(str(input("Type anything: ")))

# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.

def pythag(a, b):
    hypotenuse = (int(a)**2 + int(b)**2)**0.5
    print(hypotenuse)

pythag(int(input("Enter one side length of your triangle: ")), input("Enter another side length of your triangle: "))

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.

def test(one, two, three):
    if one >= two and one >= three:
        print(one, "is the largest")
    elif two >= one and two >= three:
        print(two, "is the largest")
    else:
        print(three, "is the largest")
    if one <= two and one <= three:
        print(one, "is the smallest")
    elif two <= one and two <= three:
        print(two, "is the smallest")
    else:
        print(three, "is the smallest")
    average = round((int(one + two + three)/3),2)
    print(average, "is the average")

test(int(input("Enter one number: ")), int(input("Enter another number: ")), int(input("Enter another number: ")))

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.
import math

def calculate(x):
    answer = math.e**x
    print(round(answer,5))

calculate(-1)
calculate(0)
calculate(1)
calculate(2)
calculate(3)

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)

import random
def integer(x):
    x *= 10
    if x < 1:
        x += 1
    print(round(x))

integer(random.random())

# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def sum_and_product(x,y):
    return x+y, x*y

sum_and_product(5,6)