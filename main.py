def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z ničlo!"
    return a / b

# Tukaj se začne nova koda
while True:
    print("\n--- Mini kalkulator ---")
    print("1 = +, 2 = -, 3 = *, 4 = /, 0 = IZHOD")
    izbira = input("Izbira: ")

    if izbira == "0":
        print("Nasvidenje!")
        break
    
    if izbira in ("1", "2", "3", "4"):
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        
        if izbira == "1": print(f"Rezultat: {sestej(x, y)}")
        elif izbira == "2": print(f"Rezultat: {odstej(x, y)}")
        elif izbira == "3": print(f"Rezultat: {pomnozi(x, y)}")
        elif izbira == "4": print(f"Rezultat: {deli(x, y)}")
    else:
        print("Neveljavna izbira!")