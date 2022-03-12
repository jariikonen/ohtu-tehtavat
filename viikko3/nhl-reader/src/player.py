import requests
from operator import attrgetter


class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
    
    def __str__(self):
        return (
            f'{self.name:20} {self.team:3} '
            f'{str(self.goals):>2} + {str(self.assists):>2} = '
            f'{str(self.points):>2}'
        )


class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player_dict in self.reader.response:
            player = Player(
                player_dict['name'], player_dict['nationality'],
                player_dict['team'], player_dict['goals'], player_dict['assists'])
            players.append(player)

        return sorted(
                list(filter(lambda p: p.nationality == nationality, players)),
                key=attrgetter('points'), reverse=True)
