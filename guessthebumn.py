correctNumber = 6

print("Guess a number:")

while True:
    guess = input()
    guess = int(guess)
    print("You guessed " + str(guess))

    if guess > correctNumber:
        print("TOO BIG")
    elif guess < correctNumber:
        print("TOO SMALL")
    else:
        print("CORRECT")
        break  # Exit the loop when the guess is correct

