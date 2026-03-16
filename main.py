def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: Deljenje z 0 ni dovoljeno!"
    return a / b

# Glavna zanka programa (Naloga #3)
while True:
    print("\n--- Mini kalkulator ---")
    print("1 = seštevanje")
    print("2 = odštevanje")
    print("3 = množenje")
    print("4 = deljenje")
    print("0 = IZHOD")
    
    izbira = input("\nIzberi operacijo (0-4): ")

    # Preverimo, če želi uporabnik končati (Naloga #3)
    if izbira == "0":
        print("Hvala, ker si uporabljal kalkulator. Nasvidenje!")
        break

    # Preverimo, če je izbira veljavna
    if izbira in ("1", "2", "3", "4"):
        try:
            x = float(input("Vnesi prvo število: "))
            y = float(input("Vnesi drugo število: "))
            
            # Lepši izpisi rezultatov (Naloga #4)
            if izbira == "1":
                print(f"\nRezultat: {x} + {y} = {sestej(x, y)}")
            elif izbira == "2":
                print(f"\nRezultat: {x} - {y} = {odstej(x, y)}")
            elif izbira == "3":
                print(f"\nRezultat: {x} * {y} = {pomnozi(x, y)}")
            elif izbira == "4":
                rezultat = deli(x, y)
                if isinstance(rezultat, str): # Če je napaka (tekst)
                    print(f"\n{rezultat}")
                else:
                    print(f"\nRezultat: {x} / {y} = {rezultat}")
        
        except ValueError:
            print("\nNapaka: Prosim vnesi številko!")
    else:
        print("\nNeveljavna izbira, poskusi ponovno.")