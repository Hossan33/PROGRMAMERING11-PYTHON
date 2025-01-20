while True:
    user_input = input("Skriv något: ")
    try:
        number = int(user_input)
        print(f"Du skrev in ett giltigt tal: {number}")
        break
    except ValueError:
        print("Det där var inte ett giltigt tal, försök igen.")
