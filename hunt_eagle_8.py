#!/usr/bin/env python3
"""a program that prints all prime numbers a user may want."""


def is_prime(number):
    """ Use the trial division algorithm to determine if number is prime

    Args: 
        number (int)

    Returns:
        bool: True if prime, False if not    
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_prime_numbers(n):
    """Get n prime numbers and return a list

    Args:
        n (int) : number of prime numbers to append to array

    Returns: 
        list (int) : Array of ints that are prime
    """
    prime_numbers = []

    i = 2
    while len(prime_numbers) <= n:
        if is_prime(i):
            prime_numbers.append(i)
        i += 1

    return prime_numbers


def get_user_input_and_display_prime_numbers():
    """Get user's desired amout of prime number then print it. If number is 
    larger than 100000 then the program will ask the user to confirm they want 
    to print that many prime numbers

    Args: 
        None

    Returns: 
        None
    """

    selected_amount_of_prime_numbers = int(input(
        'Enter the amount of prime numbers you want to display: '))

    if selected_amount_of_prime_numbers > 100000:
        confirm = input('You have selected a large amount of prime numbers. \
Are you sure you want to continue? (y/n): ')

        confirm = confirm.lower()
        if confirm == "y":
            print(f"\nDisplaying an array of {selected_amount_of_prime_numbers} prime numbers: \n",
                  get_prime_numbers(selected_amount_of_prime_numbers))
        else:
            exit()

    print(f"\nDisplaying an array of {selected_amount_of_prime_numbers} prime numbers:",
          get_prime_numbers(selected_amount_of_prime_numbers))


get_user_input_and_display_prime_numbers()
