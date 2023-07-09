import json

def film_kayıt():
    film_adi = input("Film adını girin:")

    film_liste = []

    with open("film_liste.txt", "r") as dosya:
        film_liste = json.load(dosya)

    film_liste.append(film_adi)

    with open("film_liste.txt", "w") as dosya:
        json.dump(film_liste, dosya)
    print("Film kaydedildi.")

film_kayıt()