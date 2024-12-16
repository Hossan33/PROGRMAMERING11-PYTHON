 def fråga_med_svarsalternativ(fråga, alternativ, rätt_svar):
    while True:
        print(fråga)
        for alternativ_nummer, alternativ_text in alternativ.items():
            print(f"{alternativ_nummer}. {alternativ_text}")
        svar = input("Välj ett alternativ (1, 2 eller 3): ")
        if svar in alternativ:
            if svar == rätt_svar:
                print("Rätt svar!\n")
                return 1
            else:
                print("Fel svar.\n")
                return 0
        else:
            print("Ogiltigt val, försök igen.\n")

def frågesport():
    poäng = 0
    print("Välkommen till frågesporten!\n")

    # Fråga 1
    poäng += fråga_med_svarsalternativ(
        "Vad är huvudstaden i Sverige?",
        {'1': 'Göteborg', '2': 'Stockholm', '3': 'Malmö'},
        '2'
    )

    # Fråga 2
    poäng += fråga_med_svarsalternativ(
        "Vilket år sjönk Titanic?",
        {'1': '1912', '2': '1920', '3': '1918'},
        '1'
    )

    # Fråga 3
    poäng += fråga_med_svarsalternativ(
        "Vilket är det största planet i vårt solsystem?",
        {'1': 'Jorden', '2': 'Mars', '3': 'Jupiter'},
        '3'
    )

    # Resultat
    print(f"Du fick {poäng} poäng av 3 möjliga!\n")
    
    if poäng == 3:
        print("Fantastiskt! Du fick alla rätt!")
    elif poäng == 2:
        print("Bra jobbat! Du fick de flesta rätt!")
    else:
        print("Bra försök, men du kan nog bättre!")

def spela_igen():
    while True:
        svar = input("Vill du spela igen? (ja/nej): ").lower()
        if svar == "ja":
            return True
        elif svar == "nej":
            return False
        else:
            print("Ogiltigt val, skriv 'ja' eller 'nej'.\n")

def main():
    while True:
        frågesport()
        if not spela_igen():
            print("Tack för att du spelade!")
            break

# Starta spelet
main()
