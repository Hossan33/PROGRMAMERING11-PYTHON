import random


target_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Gissa ett tal mellan 1 och 100: "))
        
        if guess < target_number:
            print("För lågt! Försök igen.")
        elif guess > target_number:
            print("För högt! Försök igen.")
        else:
            print("Grattis! Du gissade rätt!")
            break
    except ValueError:
        print("Det där var inte ett giltigt tal. Försök igen.")
