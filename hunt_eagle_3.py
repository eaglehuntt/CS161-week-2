#!/usr/bin/env python3
"""Modified previous program so only the users Alice and Bob are greeted with their names."""

def get_and_greet_alice_or_bob():
    """ Get name and print a greeting if name is alice or bob

    Args: 
        None
    
    Returns:
        None
    """
    name = input("What is your name? ")

    if name == 'Alice' or name == 'Bob':
        print(f'Greetings, {name}!')
    else:
        print('No greeting for you.')

get_and_greet_alice_or_bob()
