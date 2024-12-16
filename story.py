def start_berattelse():
    print("Hej hej!")
    print("Du står inne på ica.")
    print("Till vänster ser du en cola zero.")
    print("Till höger ser du en vanlig cola med socker.")
    val1 = input("Vill du ha cola zero (1) eller vanlig cola (2)? ")
    
    if val1 == '1':
        zero_berattelse()
    elif val1 == '2':
        cola_berattelse()
    else:
        print("Det är inte ett giltigt val. Försök igen.")
        start_berattelse()

def zero_berattelse():
    print("Du går fram mot cola zero och tar upp den.")
    print("Du går fram till kassan och köper den.")
    print("Du kan antingen dricka den (1) eller ge den til en hemlös som var törstig (2).")
    val2 = input("Vad vill du göra? ")
    
    if val2 == '1':
        print("Du öppnar burken och smakar. .")
        print("Plötsligt känner du en äcklig smak av fejk socker som sätter sig på tungan och smakar skit")
        print("Du slänger nu iväg din burk av ilska och inser att du tog helt fel val.")
    elif val2 == '2':
        print("Du försöker ge iväg den till en hemlös, men ingen vill ta emot den då sockerfri dricka är vidrigt, så du slänger iväg din burk bara. ")
        start_berattelse()
    else:
        print("Det är inte ett giltigt val. Försök igen.")
        zero_berattelse()

def cola_berattelse():
    print("Du går fram till cola burken och plockar upp den.")
    print("Du vandrar fram till kassan och köper den.")
    print("Du kan antingen dricka colan nu (1) eller hälla ut all dricka och panta. (2).")
    val3 = input("Vad vill du göra? ")
    
    if val3 == '1':
        print("Du smakar på din cola och tänker wow, vad god.")
        print("Du inser att du gjort rätt val och inte tagit den äckliga utan socker.")
        print("Du lever nu lycklig i resten av ditt liv. ")
    elif val3 == '2':
        print("Du bestämmer dig för att hälla ut colan och panta den.")
        print("Du förstår nu att de kanske inte var så smart. .")
        print("Men du fick iaf 1 kr.")
    else:
        print("Det är inte ett giltigt val. Försök igen.")
        cola_berattelse()

# Starta berättelsen
start_berattelse()
