#!/usr/bin/env python3
"""Modified the previous program so only multiples of three or five are considered in the sum"""

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter an integer only.")

for i in range(1, n + 1):  # n + 1 so we have n's value included
    if i % 3 == 0 or i % 5 == 0:  # check if i is / by 3 or 5
        print(i)
