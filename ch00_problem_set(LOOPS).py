#18/22
# LOOPS (22pts TOTAL)

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
a = 1
b = 1
while a < 1000 and b < 1000:
    print(a)
    print(b)
    a += b
    b += a

# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly

import random

x = random.randrange(1,1001)
done = False
while not done:
    guess = int(input("Guess the number: "))
    if guess < x:
        print("Higher")
    elif guess > x:
        print("Lower")
    elif guess == x:
        done = True
print("You guessed it!")

# Lee - Help the user out.  Higher and Lower are not great feedback.  Is the number I guessed higher or is the number I am supposed to guess higher? (-1)

# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

c = [0]
percent = 0
for i in range(10000):
    x = [0]
    for i in range(1, 6):
        a = random.randrange(1, 7) / i
        x.append(a * i)
        if a * i < x[i - 1]:
            percent += 1
    c.append(x)

percent /= 50000
print("The probability of each roll being greater than or equal to the previous value: ", (str(percent * 100) + "%"))

# Lee - This one doesn't work correctly.  In the for loop, you divide the random number by i.  That makes it a fraction that changes through the loop, not a random roll at all.  Percent is a bad variable name for a tracking number.  You divided percent by 50000.  Where does that come from (-3)

# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
done = False
while not done:
    a = random.randrange(1,10)
    b = random.randrange(10)
    c = random.randrange(10)
    d = random.randrange(1,10)
    if (d*1000) + (c*100) + (b*10) + a == 4*((a*1000) + (b*100) + (c*10) + d):
        done = True
    else:
        a = random.randrange(1, 10)
        b = random.randrange(10)
        c = random.randrange(10)
        d = random.randrange(1, 10)

print(a,b,c,d)

numbers = []
done = False
while not done:
    for i in range(4):
        if i == 0 or i == 3:
            x = random.randrange(1,10)
        else:
            x = random.randrange(0,10)
        numbers.append(x)
    if (int(numbers[3]))*1000 + (int(numbers[2]))*100 + (int(numbers[1]))*10 + int(numbers[0]) == 4*((int(numbers[0]))*1000 + (int(numbers[1]))*100 + (int(numbers[2]))*10 + (int(numbers[3]))):
        done = True
    else:
        del numbers[:]

print(numbers)

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(1,10):
                if int(str(d)+str(c)+str(b)+ str(a)) == 4 * int(str(a) + str(b) + str(c) + str(d)):
                    print(a,b,c,d)
