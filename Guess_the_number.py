import random

def guess(x):
    random_number=random.randint(1, x)
    guess=0
    while random_number!=guess:
        guess=int(input(f'Guess between 1 and {x}: '))
        if  random_number > guess:
            print('Sorry!Guess again!Too low')
        elif  random_number < guess:
            print('Sorry!Guess again!Too high')
    print(f'Congratulations! You guessed the {random_number} number correctly!')

guess(10)


