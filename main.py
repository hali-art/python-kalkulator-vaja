def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z 0!"
    return a / b

# Glavna zanka, ki drži program pri življenju
while True:
    print("\n--- GLAVNI MENI KALKULATORJA ---")
    print("1: Seštevanje (+)")
    print("2: Odštevanje (-)")
    print("3: Množenje (*)")
    print("4: Deljenje (/)")
    print("0: IZHOD IZ PROGRAMA")
    
    izbira = input("\nIzberi možnost: ")

    if izbira == "0":
        print("Zapiranje programa... Nasvidenje!")
        break # Prekine while zanko in konča program

    if izbira in ("1", "2", "3", "4"):
        try:
            x = float(input("Vnesi prvo število: "))
            y = float(input("Vnesi drugo število: "))
            
            if izbira == "1":
                print(f"REZULTAT: {x} + {y} = {sestej(x, y)}")
            elif izbira == "2":
                print(f"REZULTAT: {x} - {y} = {odstej(x, y)}")
            elif izbira == "3":
                print(f"REZULTAT: {x} * {y} = {pomnozi(x, y)}")
            elif izbira == "4":
                print(f"REZULTAT: {x} / {y} = {deli(x, y)}")
        except ValueError:
            print("Napaka: Vnesi veljavno številko!")
    else:
 feature/vaja-amend
        print("Napačna izbira!")

        # Testni komentar za amend

        

        print("Neveljavna izbira, poskusi znova.")
 main
