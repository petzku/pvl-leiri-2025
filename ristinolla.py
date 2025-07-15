def numerosta_pelaaja(x):
    if x == 1:
        return "X"
    elif x == 2:
        return "O"
    else:
        return "-"


def tulosta_kenttä(kenttä: list[list[int]]):
    for row in kenttä:
        # print(" ".join(numerosta_pelaaja(x) for x in row))
        # print(row[0], row[1], row[2])
        for ruutu in row:
            print(numerosta_pelaaja(ruutu), end=" ")
        print()


def kysy_ruutu(vuoro):
    print(f"Vuorossa {numerosta_pelaaja(vuoro)}.")
    while True:
        ruutu = input("Mihin ruutuun pelataan? (h = help) ")
        match ruutu:
            case "h":
                print("0 1 2")
                print("3 4 5")
                print("6 7 8")
            case r if r.isdigit() and 0 <= int(r) <= 8:
                num = int(r)
                # hassua modulo huijausta
                return (num // 3, num % 3)
            case default:
                print("Tuo ei ole ruutu!")


def onko_voitto(kenttä):
    # palautetaan 0 jos peli on vielä käynnissä
    # 1 tai 2 jos toinen voittaa
    # -1 jos tasapeli

    # tarkastetaan rivit
    for row in kenttä:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    # ja sarakkeet
    for i in range(len(kenttä[0])):
        if (kenttä[0][i] == kenttä[1][i] == kenttä[2][i]) and kenttä[0][i] != 0:
            return kenttä[0][i]
    # ja vinot
    if (kenttä[0][0] == kenttä[1][1] == kenttä[2][2]) and kenttä[0][0] != 0:
        return kenttä[0][0]
    if (kenttä[0][2] == kenttä[1][1] == kenttä[2][0]) and kenttä[0][2] != 0:
        return kenttä[0][2]

    # onko kenttä täynnä?
    # if any(x == 0 for row in kenttä for x in row):
    #     return 0
    # else:
    #     return -1
    for row in kenttä:
        for x in row:
            if x == 0:
                return 0
    return -1


def main():
    kenttä = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    # aloittaja on X
    vuoro = 1

    while not onko_voitto(kenttä):
        tulosta_kenttä(kenttä)
        print()

        # kysytään ruutua kunnes löytyy tyhjä
        while True:
            x, y = kysy_ruutu(vuoro)
            if kenttä[x][y] == 0:
                break
            else:
                print("Tuohon on jo pelattu!")

        # merkitään ruutuun haluttu numero
        kenttä[x][y] = vuoro
        # vuoro = 2 if vuoro == 1 else 1
        # sama kuin:
        if vuoro == 1:
            vuoro = 2
        else:
            vuoro = 1

    print()
    print("Peli ohi!")
    print()
    tulosta_kenttä(kenttä)
    print()
    voittaja = onko_voitto(kenttä)
    if voittaja == -1:
        print("Tasapeli!")
    else:
        print("Voittaja:", numerosta_pelaaja(voittaja))


if __name__ == "__main__":
    main()
