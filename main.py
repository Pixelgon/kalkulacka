# Kalkulacka na obycejne operace a na vzorce
# Vytvoril Matej Matejka
import math

print("|Kalkulačka|")
print("1. obyčejný příklad")
print("2. Různá tělesa")
volba = int(input("Co potřebujete spočítat?: "))
match volba:
    case 1:
        cisloa = int(input("Zadejte první číslo: "))
        cislob = int(input("Zadejte druhé číslo: "))
        print("1. Součet")
        print("2. Rozdíl")
        print("3. Součin")
        print("4. Dělení")
        print("5. Dělení se zbytkem")
        print("6. Mocnina")
        print("7. Odmocnina")
        operace = int(input("Vyberte operaci: "))

        match operace:
            # Soucete cisla A a B
            case 1:
                print("Součet: ", cisloa, "+", cislob, "=", cisloa + cislob)
            # Rozdil cisla A a B
            case 2:
                print("Rozdíl: ", cisloa, "-", cislob, "=", cisloa - cislob)
            # Soucin cisla A a B
            case 3:
                print("Součin: ", cisloa, "*", cislob, "=", cisloa * cislob)
            # Deleni cisla A
            case 4:
                print("Dělení: ", cisloa, "/", cislob, "=", cisloa / cislob)
            # Deleni cisla A se zbytkem
            case 5:
                print("Dělení se zbytkem: ", cisloa, "%", cislob, "=", cisloa // cislob, "(", cisloa % cislob, ")")
            # Mocnina
            case 6:
                print("Mocnina: ", "=", cisloa ** cislob)
            # Odmocnina
            case 7:
                print("Odmocnina: ", "=", cislob ** (1/cisloa))
    case 2:
        print("1. Čtverec")
        print("2. Obdelík")
        print("3. Kruh")
        tvar = int(input("Vyberte tvar: "))
        match tvar:
            # Ctverec
            case 1:
                stranaA = float(input("Zadejte stranu A v centimetrech: "))
                print("1. Obvod")
                print("2. Obsah")
                print("3. Úhlopříčka")
                volbaVzorceCtverec = int(input("Vyberte vzorec: "))
                match volbaVzorceCtverec:
                    case 1:
                        print("Obvod čtverce je: ", stranaA * 4, "cm")
                    case 2:
                        print("Obsah čtverce je: ", stranaA * stranaA, "cm²")
                    case 3:
                        print("Úhlopříčka čtverce je: ", stranaA * math.sqrt(2), "cm")
            # Obdelnik
            case 2:
                stranaA = float(input("Zadejte stranu A v centimetrech: "))
                stranaB = float(input("Zadejte stranu B v centimetrech: "))
                print("1. Obvod")
                print("2. Obsah")
                print("3. Úhlopříčka")
                volbaVzorceObdelnik = int(input("Vyberte vzorec: "))
                match volbaVzorceObdelnik:
                    case 1:
                        print("Obvod obdelníku je: ", stranaA * 2 + stranaB * 2, "cm")
                    case 2:
                        print("Obsah obdelníku je: ", stranaA * stranaB, "cm²")
                    case 3:
                        print("Úhlopříčka obdelníku je: ", stranaA**2 + 2**stranaB, "cm")
            # Kruh
            case 3:
                polomerR = float(input("Zadejte poloměr v centimetrech: "))
                print("1. Obvod")
                print("2. Obsah")
                print("3. Průměr")
                volbaVzorceKruh = int(input("Vyberte vzorec: "))
                match volbaVzorceKruh:
                    case 1:
                        print("Obvod kruhu je: ", 2 * math.pi * polomerR, "cm")
                    case 2:
                        print("Obsah kruhu je: ", math.pi * polomerR ** 2, "cm²")
                    case 3:
                        print("Průměr kruhu je: ", polomerR * 2, "cm")
exit()

