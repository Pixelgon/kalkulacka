# todo Přidat 3 3D nebo 2D tělesa UI

print("| Kalkulačka |")
print("1. obyčejný příklad")
print("2. Různá tělesa")
volba = int(input("Co potřebujete spočítat?:"))
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
            case 1:
                print("Součet: ", cisloa, "+", cislob, "=", cisloa + cislob)
            case 2:
                print("Rozdíl: ", cisloa, "-", cislob, "=", cisloa - cislob)
            case 3:
                print("Součin: ", cisloa, "*", cislob, "=", cisloa * cislob)
            case 4:
                print("Dělení: ", cisloa, "/", cislob, "=", cisloa / cislob)
            case 5:
                print("Dělení se zbytkem: ", cisloa, "%", cislob, "=", cisloa // cislob, "(", cisloa % cislob, ")")
            case 6:
                print("Mocnina: ", "=", cisloa ** cislob)
            case 7:
                print("Odmocnina: ", "=", cislob ** (1/cisloa))
    case 2:
        print("1. Čtverec")
        print("2. Kruh")
        print("3. Obdelník")

exit()

