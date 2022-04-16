import sys
from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    argument = sys.argv[1] if len(sys.argv) > 1 else ""

    matcher = None

    if argument:
        print(f"Kysely {argument}: ", end="")
        argument = int(argument)

        if argument == 1:
            print("tehtävä 2 (ensimmäinen tarkistuskysely)")
            matcher = And(
                Not(HasAtLeast(1, "goals")),
                PlaysIn("NYR")
            )
        elif argument == 2:
            print("tehtävä 2 (toinen tarkistuskysely)")
            matcher = And(
                HasFewerThan(1, "goals"),
                PlaysIn("NYR")
            )
        elif argument == 3:
            print("tehtävä 3 (ensimmäinen tarkistuskysely)")
            matcher = Or(
                HasAtLeast(30, "goals"),
                HasAtLeast(50, "assists")
            )
        elif argument == 4:
            print("tehtävä 3 (toinen tarkistuskysely)")
            matcher = And(
                HasAtLeast(40, "points"),
                Or(
                    PlaysIn("NYR"),
                    PlaysIn("NYI"),
                    PlaysIn("BOS")
                )
            )
        elif argument == 5:
            print("tehtävä 4")
            query = QueryBuilder()
            matcher = (
                query
                    .playsIn("NYR")
                    .hasAtLeast(5, "goals")
                    .hasFewerThan(10, "goals")
                    .build()
            )
        elif argument == 6:
            print("tehtävä 5 (apumuuttujilla)")
            query = QueryBuilder()
            m1 = (
                query
                    .playsIn("PHI")
                    .hasAtLeast(10, "assists")
                    .hasFewerThan(5, "goals")
                    .build()
            )
            m2 = (
                query
                    .playsIn("EDM")
                    .hasAtLeast(40, "points")
                    .build()
            )
            matcher = query.oneOf(m1, m2).build()
        elif argument == 7:
            print("tehtävä 5 (ilman apumuuttujia)")
            query = QueryBuilder()
            matcher = (
                query
                    .oneOf(
                        query.playsIn("PHI")
                            .hasAtLeast(10, "assists")
                            .hasFewerThan(5, "goals")
                            .build(),
                        query.playsIn("EDM")
                            .hasAtLeast(40, "points")
                            .build()
                    )
                    .build()
            )
        else:
            print("kyselyä ei määritetty")
            exit()
    else:
        print("Eri tehtävien tarkistukset saat antamalla "\
            "käynnistyskomennolle seuraavat komentoriviargumentit:\n\n"\
            "1: tehtävä 2 (ensimmäinen tarkistuskysely)\n"\
            "2: tehtävä 2 (toinen tarkistuskysely)\n"\
            "3: tehtävä 3 (ensimmäinen tarkistuskysely)\n"\
            "4: tehtävä 3 (toinen tarkistuskysely)\n"\
            "5: tehtävä 4\n"\
            "6: tehtävä 5 (apumuuttujilla)\n"\
            "7: tehtävä 5 (ilman apumuuttujia)\n\n"
            "Esimerkiksi: poetry run python3 src/index.py 1\n\n"
            "Seuraavat tulokset tulevat koodissa olleesta oletuskyselystä "\
            "(väh. 5 maalia, väh. 5 syöttöä, pelaa PHI).\n")

        matcher = And(
            HasAtLeast(5, "goals"),
            HasAtLeast(5, "assists"),
            PlaysIn("PHI")
        )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
