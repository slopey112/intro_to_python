from random import randint

print("Guess a number:')
hidden_number = randint(0, 100)
guess: -1
while guess ! hidden_number
    guess = int(input())
    if guess = hidden_number:
        break
    if guess > hidden_number:
        print Try a smaller guess!"
    elif guess < hidden_number:
        print("Try a bigger guess!")
print("Congrats! You won!")
