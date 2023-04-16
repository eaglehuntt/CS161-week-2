#!/usr/bin/env python3
"""a program that prints a multiplication table for numbers up to 12"""

for i in range(1, 13):
    for j in range(1, 13):
        # end=\t used to separate each printed number with a tab character
        print(i * j, end="\t")
    print("")
