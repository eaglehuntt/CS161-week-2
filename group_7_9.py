"""a guessing game where the user has to guess a secret number. After every guess the program 
tells the user whether their number was too large or too small. At the end the number of tries 
needed should be printed. It counts only as one try if they input the same number multiple times 
consecutively."""

import random


class GuessingGame:

    def __init__(self, largest_possible_number):
        self.largest_possible_number = largest_possible_number
        self.__secret_number = random.randint(1, largest_possible_number)
        self.tries = []
        # set last_guess to None to account for the first try
        self.last_guess = None
        self.record = None

    def play(self):
        print('------------------------')
        print('Guessing Game')
        print(f'Current record: {self.record}')
        print('------------------------')

        print('How to play:\n')
        print('There is a secret number. Try to guess it in the least amount of tries as possible.')
        print('A try will not count if you guess the same number consecutively.')
        print('Be careful, if you guess the same number again non-consecutively you are out luck')
        print('Good luck.')
        print('---------------------------------------------------------------------------------\n')

        while True:

            guess = self.user_guess_value()

            if self.is_secret_number(guess):
                print('\n-------\nYOU WIN!\n-------\n')

                if self.record is None or len(self.tries) < self.record:
                    self.record = len(self.tries)
                    print('New Record!')

                print(f'Total tries: {len(self.tries)}')
                print(f'\nTries: {self.tries}')

                while True:
                    play_again = input('Would you like to play again? (y/n): ')
                    if play_again == 'y':
                        self.clear_values()
                        self.play()
                    elif play_again == 'n':
                        exit()
                    else:
                        print('Invalid input')
            else:
                print(f'\nCurrent tries: {self.tries}\n')
                if guess < self.__secret_number:
                    print('Your guess was LESS than the secret number')
                else:
                    print('Your guess was MORE than the secret number')

    def user_guess_value(self):
        while True:

            try:
                guess = int(input(f'({len(self.tries)}) Enter your guess: '))

                if guess != self.last_guess:

                    # append guess to tries array if the last guess if it was not current guess
                    self.tries.append(guess)

                    # after appending, make current guess last guess
                    self.last_guess = guess

                return guess

            except ValueError:
                print('Invalid input. Select an integer.')

    def is_secret_number(self, guess):
        if guess == self.__secret_number:
            return True

    def clear_values(self):
        self.tries = []
        self.last_guess = None
        self.__secret_number = random.randint(1, self.largest_possible_number)


game = GuessingGame(100)  # secret number max is 100
game.play()
