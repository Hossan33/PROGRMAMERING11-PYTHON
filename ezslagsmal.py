import random

def battle():
    fighter_a_name = input("Ange namn för Kämpare A: ")
    fighter_b_name = input("Ange namn för Kämpare B: ")

    fighter_a = {
        'name': fighter_a_name,
        'hp': 100
    }

    fighter_b = {
        'name': fighter_b_name,
        'hp': 100
    }

    while fighter_a['hp'] > 0 and fighter_b['hp'] > 0:
        damage_a = random.randint(5, 15)
        fighter_b['hp'] -= damage_a
        print(f"{fighter_a['name']} slår {fighter_b['name']} och gör {damage_a} skada! ({fighter_b['hp']} HP kvar)")

        damage_b = random.randint(5, 15)
        fighter_a['hp'] -= damage_b
        print(f"{fighter_b['name']} slår {fighter_a['name']} och gör {damage_b} skada! ({fighter_a['hp']} HP kvar)")

    if fighter_a['hp'] <= 0 and fighter_b['hp'] <= 0:
        print("Det blev oavgjort!")
    elif fighter_a['hp'] <= 0:
        print(f"{fighter_b['name']} vinner!")
    else:
        print(f"{fighter_a['name']} vinner!")

while True:
    battle()
    play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
    if play_again != 'ja':
        print("Tack för att du spelade!")
        break
