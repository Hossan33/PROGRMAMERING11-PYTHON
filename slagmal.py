import random

class Fighter:
    def __init__(self, name, hp, strength, speed):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed

    def attack(self, other, attack_type):
        hit_chance = 0.8 if attack_type == "snabb" else 0.5
        max_damage = self.strength if attack_type == "snabb" else self.strength * 2
        if random.random() <= hit_chance:
            damage = random.randint(1, max_damage)
            other.hp -= damage
            return damage, True
        return 0, False

def get_fighter_name(fighter_num):
    while True:
        name = input(f"Skriv in namn för slagskämpe {fighter_num} (3-12 tecken): ")
        if 3 <= len(name) <= 12:
            return name
        print("Namnet måste vara mellan 3 och 12 tecken.")

def random_opponent_name():
    names = ["Brock", "Misty", "Ash"]
    return random.choice(names)

def display_ascii_art(fighter):
    if fighter == "A":
        print("""
        A:
        O
       /|\\
       / \\
        """)
    elif fighter == "B":
        print("""
        B:
        O
       /|\\
       / \\
        """)

def choose_attack():
    while True:
        choice = input("Välj attack (snabb/stark): ").lower()
        if choice in ["snabb", "stark"]:
            return choice
        print("Ogiltigt val, välj 'snabb' eller 'stark'.")

def place_bet(player_name):
    while True:
        try:
            bet = int(input(f"{player_name}, hur mycket pengar vill du satsa på din fighter? "))
            if bet > 0:
                return bet
        except ValueError:
            print("Du måste ange ett positivt heltal.")

def display_hp(fighter_a, fighter_b):
    print(f"{fighter_a.name}: {fighter_a.hp} HP")
    print(f"{fighter_b.name}: {fighter_b.hp} HP")

def battle_round(fighter_a, fighter_b):
    attack_type_a = choose_attack()
    damage_a, hit_a = fighter_a.attack(fighter_b, attack_type_a)
    if hit_a:
        print(f"{fighter_a.name} träffade {fighter_b.name} och gjorde {damage_a} skada!")
    else:
        print(f"{fighter_a.name} missade!")

    if fighter_b.hp > 0:
        attack_type_b = random.choice(["snabb", "stark"])
        damage_b, hit_b = fighter_b.attack(fighter_a, attack_type_b)
        if hit_b:
            print(f"{fighter_b.name} träffade {fighter_a.name} och gjorde {damage_b} skada!")
        else:
            print(f"{fighter_b.name} missade!")

    display_hp(fighter_a, fighter_b)

def display_leader(fighter_a, fighter_b):
    if fighter_a.hp > fighter_b.hp:
        print(f"{fighter_a.name} leder med {fighter_a.hp} HP kvar.")
    elif fighter_b.hp > fighter_a.hp:
        print(f"{fighter_b.name} leder med {fighter_b.hp} HP kvar.")
    else:
        print(f"Det är oavgjort! Båda har {fighter_a.hp} HP kvar.")

def fight(fighter_a, fighter_b, rounds):
    for round_num in range(1, rounds + 1):
        print(f"\n--- Runda {round_num} ---")
        battle_round(fighter_a, fighter_b)
        display_leader(fighter_a, fighter_b)
        if fighter_b.hp <= 0:
            print(f"{fighter_a.name} vinner!")
            return fighter_a.name
        if fighter_a.hp <= 0:
            print(f"{fighter_b.name} vinner!")
            return fighter_b.name

    if fighter_a.hp > fighter_b.hp:
        print(f"{fighter_a.name} vinner på poäng!")
        return fighter_a.name
    else:
        print(f"{fighter_b.name} vinner på poäng!")
        return fighter_b.name

def restart_game():
    choice = input("Vill du starta om spelet? (ja/nej): ").lower()
    return choice == "ja"

def start_game():
    while True:
        fighter_a_name = get_fighter_name(1)
        fighter_b_name = random_opponent_name()
        
        fighter_a = Fighter(fighter_a_name, hp=100, strength=20, speed=15)
        fighter_b = Fighter(fighter_b_name, hp=100, strength=20, speed=15)
        
        display_ascii_art("A")
        display_ascii_art("B")
        
        bet_a = place_bet(fighter_a_name)
        rounds = int(input("Hur många rundor vill du spela? (3-10): "))
        
        winner = fight(fighter_a, fighter_b, rounds)
        if winner == fighter_a_name:
            print(f"{fighter_a_name} vann och du tjänade {bet_a * 2}!")
        else:
            print(f"{fighter_a_name} förlorade och du förlorade {bet_a}...")
        
        if not restart_game():
            break

start_game()
