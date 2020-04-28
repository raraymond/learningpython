# generatoe a random number
from random import randint
import sys

low = int(sys.argv[1])
high = int(sys.argv[2])
answer = randint(low, high)
# get input from user

# check that input is a numbe 1-10
while True:
    try:
        print(answer)
        guess = int(input('guess a number: '))
        if low < guess < high:
            if guess == answer:
                print('You are a genius')
                break
        else:
            print('hey i said between 1 and 10')
    except ValueError:
        print('please enter a valid number')
        continue

# check if number is the right guess otherwise ask again
