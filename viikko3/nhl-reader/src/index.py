import requests
from operator import attrgetter
from datetime import datetime
from player import Player

def main():
    url = 'https://nhlstatisticsforohtu.herokuapp.com/players'
    response = requests.get(url).json()

    nationality = 'FIN'
    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'],
            player_dict['team'], player_dict['goals'], player_dict['assists'])
        players.append(player)

    print(
        f'Players from {"nationality"} '
        f'{datetime.today().strftime("%d.%m.%Y %H:%M:%S")}:\n')

    for player in sorted(
            list(filter(lambda p: p.nationality == nationality, players)),
            key=attrgetter('points'), reverse=True):
        print(player)

if __name__ == "__main__":
    main()
