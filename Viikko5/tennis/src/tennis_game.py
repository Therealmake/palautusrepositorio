class TennisGame:
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._equal_score()

        if self.player1_score >= 4 or self.player2_score >= 4:
            return self._end_score()

        return self._score()

    def _equal_score(self):
        if self.player1_score < 3:
            return f"{self.score_names[self.player1_score]}-All"
        return "Deuce"

    def _end_score(self):
        gap = self.player1_score - self.player2_score
        if gap == 1:
            return f"Advantage {self.player1_name}"
        if gap == -1:
            return f"Advantage {self.player2_name}"
        if gap >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _score(self):
        return f"{self.score_names[self.player1_score]}-{self.score_names[self.player2_score]}"