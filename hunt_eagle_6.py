#!/usr/bin/env python3
"""
A program that asks the user for a number n and gives them the choice
to choose between computing the sum and computing the product of 1,…,n.
"""

def get_user_choice_and_compute_result(n):
    """Recursive function that gets user choice and returns it. Calls itself if input is incorrect
    
    Args:
        n (int): number that user inputs

    Returns:
        choice (str): s | r depending on user
    """
    choice = input("Compute sum or product? (s | p) ")

    if choice == "s":
        result = sum(range(1, n + 1))
        print(f"The sum of 1 to {n} is {result}.")

    elif choice == "p":
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"The product of 1 to {n} is {result}.")

    else:
        print("Invalid choice. Please enter 's' or 'p'.")
        get_user_choice_and_compute_result(n)


def main():
    """Main wrapper function that calls everything

    Args:
        None

    Returns:
        None
    """
    while True:
        try:
            n = int(input("Enter a positive integer n: "))
            if n < 1:
                raise ValueError()
            break
        except ValueError:
            print('Enter in a positive integer.')

    get_user_choice_and_compute_result(n)

main() # call main function
