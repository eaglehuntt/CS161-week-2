#!/usr/bin/env python3
"""a program that asks the user for a number n and prints the sum of the numbers 1 to n"""

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print('Please enter an integer only.')

for i in range(1, n + 1): # n + 1 so we have n's value included
    print(i)
    