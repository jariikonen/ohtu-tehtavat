from datetime import datetime
from player import PlayerReader, PlayerStats

def main():
    url = 'https://nhlstatisticsforohtu.herokuapp.com/players'
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = 'FIN'
    players = stats.top_scorers_by_nationality(nationality)

    print(
        f'Players from {nationality} '
        f'{datetime.today().strftime("%d.%m.%Y %H:%M:%S")}:\n')

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
