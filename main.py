def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b): # DODANA FUNKCIJA
    if b == 0:
        return "Napaka: Deljenje z 0 ni mogoče!"
    return a / b

print("Pozdrav! Mini kalkulator")
print("1 = seštevanje")
print("2 = odštevanje")
print("3 = množenje")
print("4 = deljenje") # DODANO V MENI

izbira = input("Kaj želiš narediti? (1, 2, 3 ali 4): ")

if izbira == "1":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {sestej(x, y)}")
elif izbira == "2":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {odstej(x, y)}")
elif izbira == "3":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {pomnozi(x, y)}")
elif izbira == "4": # DODANA LOGIKA
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {deli(x, y)}")
else:
    print("Neveljavna izbira!")