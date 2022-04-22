from toimintalogiikka.pelimuoto import Pelimuoto


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = None

        if vastaus.endswith("a"):
            peli = Pelimuoto.luo_kaksinpeli()
        elif vastaus.endswith("b"):
            peli = Pelimuoto.luo_yksinpeli()
        elif vastaus.endswith("c"):
            peli = Pelimuoto.luo_haastava_yksinpeli()
        else:
            break

        if peli:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.suorita()

if __name__ == "__main__":
    main()
