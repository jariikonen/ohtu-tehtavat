class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1

    def get_score(self):
        score_str = ""

        if self.player1_points == self.player2_points:
            score_str = self.tie_score()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            score_str = self.deuce_score()
        else:
            score_str = self.regular_score()

        return score_str

    def tie_score(self):
        if self.player1_points == 0:
            return "Love-All"
        elif self.player1_points == 1:
            return "Fifteen-All"
        elif self.player1_points == 2:
            return "Thirty-All"
        elif self.player1_points == 3:
            return "Forty-All"
        else:
            return "Deuce"

    def deuce_score(self):
        minus_result = self.player1_points - self.player2_points

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def regular_score(self):
        return self.points_to_words(self.player1_points) + "-"\
            + self.points_to_words(self.player2_points)

    def points_to_words(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"
