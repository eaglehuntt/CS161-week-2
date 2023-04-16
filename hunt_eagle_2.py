#!/usr/bin/env python3
"""a program that asks the user for their name and greets them with their name"""

def get_and_great_name():
    """ Get name and print a greeting

    Args: 
        None
    
    Returns:
        None
    """
    name = input("What is your name? ")
    print(f'Greetings, {name}!')

get_and_great_name()
