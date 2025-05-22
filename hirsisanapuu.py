def hirsipuu():
    # Määritetään arvattava sana ja alustetaan muuttujat
    sana = "kultainennoutaja"
    arvattu = []  # Lista arvatuista kirjaimista
    yritykset = 10  # Sallittujen virheiden määrä

    print("Tervetuloa hirsipuupeliin!")
    print("_ " * len(sana))  # Tulostetaan aluksi viivat kirjainten kohdalle

    # Pelisilmukka jatkuu, kun yrityksiä on jäljellä
    while yritykset > 0:
        arvaus = input("Arvaa kirjain: ").lower()  # Otetaan kirjainarvaus

        # Tarkistetaan, että arvaus on yksi kirjain
        if not arvaus.isalpha() or len(arvaus) != 1:
            print("Anna yksi kirjain.")
            continue

        # Estetään saman kirjaimen arvaaminen uudelleen
        if arvaus in arvattu:
            print("Olet jo arvannut tämän kirjaimen.")
            continue

        arvattu.append(arvaus)  # Lisätään arvaus listaan

        # Tarkistetaan, sisältyykö kirjain sanaan
        if arvaus in sana:
            print("Oikein!")
        else:
            yritykset -= 1  # Vähennetään yrityksiä väärästä arvauksesta
            print(f"Väärin! Yrityksiä jäljellä: {yritykset}")

        # Muodostetaan tulosrivi, jossa arvattuja kirjaimia näkyy
        tulos = ""
        for kirjain in sana:
            if kirjain in arvattu:
                tulos += kirjain + " "
            else:
                tulos += "_ "

        print(tulos)  # Tulostetaan nykyinen sanan tila

        # Tarkistetaan, onko sana arvattu kokonaan
        if "_" not in tulos:
            print("Onneksi olkoon! Arvasit sanan.")
            break
    else:
        # Jos yritykset loppuvat, peli päättyy tappioon
        print(f"Hävisit! Oikea sana oli: {sana}")

# Käynnistetään peli, jos tiedostoa ajetaan suoraan
if __name__ == "__main__":
    hirsipuu()
