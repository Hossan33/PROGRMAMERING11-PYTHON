correct_password = "nopass"

while True:
    password = input("Ange lösenord: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Fel lösenord, försök igen.")
