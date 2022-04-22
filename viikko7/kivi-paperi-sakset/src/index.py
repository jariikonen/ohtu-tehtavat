from toimintalogiikka.pelimuodot.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from toimintalogiikka.pelimuodot.kps_tekoaly import KPSTekoaly
from toimintalogiikka.pelimuodot.kps_parempi_tekoaly import KPSParempiTekoaly


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = KPSPelaajaVsPelaaja()
            kaksinpeli.suorita()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = KPSTekoaly()
            yksinpeli.suorita()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.suorita()
        else:
            break


if __name__ == "__main__":
    main()
