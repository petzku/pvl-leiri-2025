## Halutaan laskea kahden numeron summa ja tulo.


def tapa_1():
    # Kysytään käyttäjältä numerot ja muunnetaan kokonaisluvuiksi.
    # Kaatuu jos käyttäjä antaa mitään muuta kuin kokonaisluvun (ml. desimaaliluvun)
    a = int(input("Anna luku: "))
    b = int(input("Anna toinen luku: "))

    return a, b


def tapa_2():
    # Hyväksytään kanssa desimaalit.
    # Edelleen, kaatuu jos tulee väärä input.
    a = float(input("Anna luku: "))
    b = float(input("Anna toinen luku: "))

    return a, b


def tapa_3():
    # Varmempi tapa: kysytään käyttäjältä kunnes saadaan kelvollinen luku.
    # try/except antaa napata virheet, ennen kuin ohjelma kaatuu kokonaan.
    while True:
        try:
            a = float(input("Anna luku: "))
            # Jos saatiin kelvollinen arvo, koodi pääsee tähän asti, ja voidaan lopettaa kysyminen.
            break
        except ValueError:
            # Jos ei saatu kelvollista arvoa, tulee virhe. Ilmoitetaan käyttäjälle ja kysytään uudestaan.
            print("Tuo ei ole kelvollinen luku! Yritähän uudestaan.")

    while True:
        try:
            b = float(input("Anna toinen luku: "))
            break
        except ValueError:
            print("Tuo ei ole kelvollinen luku! Yritähän uudestaan.")

    return a, b


def tapa_4():
    # Toinen käyttötarkoitus: yritetään käyttää kokonaislukua, jos voidaan.

    # Kysytään ensin käyttäjältä lukua, ja talletetaan vastaus muuttujaan.
    # Näin vältetään kysymästä samaa asiaa varten useasti.
    a_str = input("Anna luku: ")
    try:
        # Yritetään lukea kokonaislukua...
        a = int(a_str)
    except ValueError:
        # ...ja kokeillaan liukulukuna jos ei onnistunut
        a = float(a_str)

    # Ja sama uudestaan:
    b_str = input("Anna toinen luku: ")
    try:
        b = int(b_str)
    except ValueError:
        b = float(b_str)

    return a, b


def tapa_5():
    # Yhdistetään: kokonaisluku, jos voidaan; kysellään kunnes saadaan ainakin _joku_ luku.
    while True:
        a_str = input("Anna luku: ")
        try:
            a = int(a_str)
            break
        except ValueError:
            try:
                a = float(a_str)
                break
            except ValueError:
                print("Tuo ei ole kelvollinen luku! Yritähän uudestaan.")

    while True:
        b_str = input("Anna toinen luku: ")
        try:
            b = int(b_str)
            break
        except ValueError:
            try:
                b = float(b_str)
                break
            except ValueError:
                print("Tuo ei ole kelvollinen luku! Yritähän uudestaan.")

    return a, b


def main():
    tapa = input("Mitä tapaa käytetään? (1-5) ")
    match tapa:
        case "1":
            a, b = tapa_1()
        case "2":
            a, b = tapa_2()
        case "3":
            a, b = tapa_3()
        case "4":
            a, b = tapa_4()
        case "5":
            a, b = tapa_5()
        case default:
            print("Ei käy")
            return

    print(f"Summa: {a} + {b} = {a + b}")
    print(f"Tulo: {a} * {b} = {a * b}")


if __name__ == "__main__":
    main()

# Ai niin ja sit: näin ei voi kuitenkaan tehdä
def foo(x):
    try:
        # Tämä saadaan kiinni
        int(x)
    except ValueError:
        # Tästä tulee aina virhe, koska ei olla enää try:n sisässä
        int(x)
    except ValueError:
        print("tupla-except")
