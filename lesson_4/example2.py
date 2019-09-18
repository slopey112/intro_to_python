print('Let\'s play a game! Try to guess my number...')
try:
    guess = int(input('Enter a number between 0 and 100: '))
except NumberFormatException:
    print('Uh oh, that\'s not a number.')

if not (guess <= 100 and guess >= 0):
    print('Hey! You\'re cheating! The number must be between 0 and 100.')
elif guess < 78:
    print('Try entering a higher number...')
elif guess > 78:
    print('Try entering a lower number...')
else:
    print('You win!')
