from unittest import result


def spel():
    correct_answer = 7
    score = 0

    print("matte: x * 6 = 42")
    gissning = input("vad är x: ")

    if not gissning.isdigit():
        print("fel, skriv ett nummer")
        return


    guess = int(gissning)

    if guess == correct_answer:
        print("+ 1 poäng")
        score += 1
        print(f"din poäng: {score}")
    else:
        result = guess * 6
        print (f"nej, {guess} * 6 = {result}")
        if guess > correct_answer:
            print("för högt")
        else:
            print ("för lågt")


spel()





    
    






