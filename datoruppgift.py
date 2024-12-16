
datorer = ["Dator 1", "Dator 2", "Dator 3", "Dator 4", "Dator 5"]
service = []  
max_service = 3 

def visa_listor():
    print("\nTillgängliga datorer:")
    for i, dator in enumerate(datorer):
        print(f"{i + 1}. {dator}")
    
    print("\nDatorer på service:")
    for i, dator in enumerate(service):
        print(f"{i + 1}. {dator}")

while len(service) < max_service:
    visa_listor()
    
    val = int(input("\nAnge numret på datorn du vill skicka på service: ")) - 1
    
    if 0 <= val < len(datorer): 
       
        dator_som_ska_pa_service = datorer.pop(val)
        service.append(dator_som_ska_pa_service)
        print(f"\n{dator_som_ska_pa_service} har skickats på service.")
    else:
        print("Ogiltigt val, försök igen.")

print("\nMax antal datorer på service. Programmet avslutas.")
