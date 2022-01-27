import random

def guess_a_number(a):
    random_number = random.randint(1, a)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {a}: '))
        if guess_number < random_number:
            print('Sorry, guess again. Too low.')
        elif guess_number > random_number:
            print('Sorry, guess again. Too high. ')
    
    print(f'YAY! Congratulations! You have guessed the number {random_number} correctly!')


def computer_guess_number(b):
    low = 1
    high = b
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = low
        feedback = input(f'Is {guess_number} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1
    print(f'Yay! The computer guessed your number {guess_number} correctly!')


print(computer_guess_number(100))