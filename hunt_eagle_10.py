#!/usr/bin/env python3
"""
A program that computes the sum of an alternating series where each element of the series 
is an expression of the form ((-1)^k-1)(2*k-1) for each value of k from 1 to 1 million *4
"""
# I am not good at math and had to do a lot of research for this
# I asked my girlfriend and chatgpt for math help and I think you are asking for
# Leibniz formula for π

total = 0
for k in range(1, 10000000+1):
    term = ((-1)**(k+1)) / (2*k-1)
    total += term
print (total * 4)
