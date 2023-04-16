#!/usr/bin/env python3
"""
A guessing game where the user has to guess a secret number.
I modified the rules slightly.

1) Before the game starts, the player can specify the highest possible value
for the secret number

2) The point of the game is to beat the computer at guessing the secret number.
The computer will calculate the guesses to beat by doing a binary search

3) After every guess the program tells the user whether their number was too 
large or too small.

4) If a player inputs the same guess twice then it will not count as a try.
But if they do, then that will count."""

import random


class GuessingGame:

    def __init__(self, largest_possible_number):
        """init function

        Args:
            self: instance of class
            largest_possible_number (int) : The largest the secret number can be

        Returns:
            None
        """
        self.largest_possible_number = largest_possible_number

        # private secret number variable. So player cannot cheat
        self.__secret_number = random.randint(1, largest_possible_number)
        self.player_guesses = []

        # set last_guess to None to account for the first guess.
        self.last_guess = None

        self.cpu_guesses = []
        self.guesses_to_beat = self.get_cpu_guesses()

    def play(self):
        """Main function that starts the game. It prints the intro, and calls 
        the run_game function.

        Args:
            self: instance of class

        Returns: 
            None
        """
        print('---------------')
        print('Guessing Game')
        print('---------------')

        print('You are in a guessing match against the computer!')
        print('Find the secret number in less guesses than the computer to win')
        print(
            f"Largest possible secret number: {self.largest_possible_number}\n\n")

        self.run_game()

    def run_game(self):
        """Recursive function that is the main logic for the game.

        1. It gets the player's guess

        2. Compares players's total guesses to the CPU's total guesses to
        determine if the player can keep guessing. If they can, the function 
        calls itself recursively until they can't

        3. Determines if players wins/draws/loses and prints screen accordingly

        Args:
            self: instance of class

        Returns:
            None
        """
        remaining = self.guesses_to_beat - len(self.player_guesses)
        guess = self.get_user_guess(remaining)
        # this was a bug fix because it would give the player an extra guess
        remaining += -1

        if self.is_secret_number(guess) and remaining >= 1:
            self.show_end_screen('WIN')
        elif self.is_secret_number(guess) and remaining == 0:
            self.show_end_screen('DRAW')
        else:
            if remaining > 0:
                print(f'\nYour guesses: {self.player_guesses}\n')

                if guess < self.__secret_number:
                    print(f'{guess} was too LOW')
                else:
                    print(f'{guess} was too HIGH')

                self.run_game()
            else:
                self.show_end_screen('LOSE')

    def show_end_screen(self, status):
        """Displays the end screen with scores from the player and CPU

        Args: 
            self: instance of class
            status (str): WIN/DRAW/LOSE used to print end screen

        Returns:
            None
        """
        if status == "WIN":
            print('\n-------\nYOU WIN!\n-------\n')
            print(
                f'YOU: {len(self.player_guesses)} attempts {self.player_guesses}')
            print(f'CPU: {self.guesses_to_beat} attempts {self.cpu_guesses}')

        elif status == "DRAW":
            print('\n-------\nDRAW!\n-------\n')
            print(
                f'YOU: {len(self.player_guesses)} attempts {self.player_guesses}')
            print('CPU: {self.guesses_to_beat} attempts {self.cpu_guesses}')

        else:
            print('\n-------\nYOU LOSE!\n-------\n')
            print(f'The secret number was: {self.__secret_number}\n')
            print(
                f'YOU: {len(self.player_guesses)} attempts {self.player_guesses}')
            print(f'CPU: {self.guesses_to_beat} attempts {self.cpu_guesses}')

    def get_cpu_guesses(self):
        """Binary searched used to get the CPU's scores
        1. Initializes a guess counter and memory array. The memory array is
        just a list of numbers from 1 to the selected max secret number

        2. When doing the binary search, every step before the pointer is moved
        it appends to the class' cpu_guesses array. This will be displayed to
        the player at the end of the game. It also adds to the counter

        3. Once the search is done, we break the loop and return the counter

        Args:
            self: instance of class

        Returns:
            guess_counter (int): the amount of guesses the binary search did.
            I could have just made this function return None and have the
            class variable self.guesses_to_beat be the length of the 
            self.cpu_guesses array, but I thought this was cleaner becasue I 
            could call this function when I initialize the class opposed to 
            calling the function later. I'm not sure which approach would be 
            better, maybe you have some thoughts?
        """
        guess_counter = 0
        memory = [i for i in range(1, self.largest_possible_number + 1)]
        target = self.__secret_number
        l = 0
        r = self.largest_possible_number

        while l <= r:
            i = (l + r) // 2
            if memory[i] == target:
                self.cpu_guesses.append(memory[i])
                guess_counter += 1
                break
            elif memory[i] < target:
                self.cpu_guesses.append(memory[i])
                guess_counter += 1
                l = i + 1
            elif memory[i] > target:
                self.cpu_guesses.append(memory[i])
                guess_counter += 1
                r = i - 1
        else:
            # we should never be in this case.
            # the array of values will always contain the target,because it will
            # have all values from 1 to highest possible.
            # this is just for good measure
            print('There has been a critical error with the game.')
        return guess_counter

    def get_user_guess(self, remaining):
        """Gets the user's guess with error checking

        Args:
            self: instance of class

        Returns:
            guess (int): the user's attempt to guess the secret number
        """

        while True:
            try:
                guess = int(
                    input(f'Enter your guess ({remaining} remaining): '))

                if guess != self.last_guess:

                    # append guess to guesses array if the last guess if it
                    # was not current guess
                    self.player_guesses.append(guess)

                    # after appending, make current guess last guess
                    self.last_guess = guess

                return guess

            except ValueError:
                print('Invalid input. Select an integer.')

    def is_secret_number(self, guess):
        """Check if the guess is the secret number

        Args:
            self: instance of class
            guess (int): user's guess

        Returns:
            bool: True if guess is the secret number, False if not
        """
        if guess == self.__secret_number:
            return True


difficulty = int(input('Enter in the largest secret number: '))

game = GuessingGame(difficulty)
game.play()
