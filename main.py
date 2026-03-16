def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z 0!"
    return a / b

zgodovina = [] # TUKAJ SE SHRANJUJEJO REZULTATI

while True:
    print("\n--- Mini kalkulator ---")
    print("1=+, 2=-, 3=*, 4=/, 0=IZHOD, 5=ZGODOVINA")
    izbira = input("Izbira: ")

    if izbira == "0":
        print("Nasvidenje!")
        break
    
    if izbira == "5":
        print("\n--- Zadnji 3 izračuni ---")
        if not zgodovina:
            print("Zgodovina je prazna.")
        for vnos in zgodovina:
            print(vnos)
        continue

    if izbira in ("1", "2", "3", "4"):
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        
        rezultat_izpisa = ""
        if izbira == "1": rezultat_izpisa = f"{x} + {y} = {sestej(x, y)}"
        elif izbira == "2": rezultat_izpisa = f"{x} - {y} = {odstej(x, y)}"
        elif izbira == "3": rezultat_izpisa = f"{x} * {y} = {pomnozi(x, y)}"
        elif izbira == "4": rezultat_izpisa = f"{x} / {y} = {deli(x, y)}"
        
        print(f"Rezultat: {rezultat_izpisa}")
        
        # Dodajanje v zgodovino in ohranjanje samo zadnjih 3
        zgodovina.append(rezultat_izpisa)
        if len(zgodovina) > 3:
            zgodovina.pop(0)
    else:
        print("Napačna izbira!")