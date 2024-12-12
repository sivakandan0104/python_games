import random
a = 0
c = random.randint(1, 100)
while True:
    guess = int(input('Enter your guess: '))
    a += 1
    if guess == c:
        print(f'You have guessed the number {c} in {a} attempts.')
        break
    elif guess > c:
        print('Your guess is greater than the value.')
    else:
        print('Your guess is smaller than the value.')
