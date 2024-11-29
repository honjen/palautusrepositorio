class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    SCORE_TIED_NAMES = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All", 3: "Deuce"}
    MIN_POINTS_FOR_ADVANTAGE = 4
    POINT_DIFFERENCE_TO_WIN = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def get_score(self):
        if self.is_tied():
            return self.get_tied_score()
        if self.is_endgame():
            return self.get_endgame_score()
        return self.get_standard_score()

    def is_tied(self):
        return self.player1_score == self.player2_score

    def get_tied_score(self):
        return self.SCORE_TIED_NAMES.get(self.player1_score, "Deuce")

    def is_endgame(self):
        return self.player1_score >= self.MIN_POINTS_FOR_ADVANTAGE or self.player2_score >= self.MIN_POINTS_FOR_ADVANTAGE

    def get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        if score_difference == -1:
            return f"Advantage {self.player2_name}"
        if score_difference >= self.POINT_DIFFERENCE_TO_WIN:
            return f"Win for {self.player1_name}"
        if score_difference <= -self.POINT_DIFFERENCE_TO_WIN:
            return f"Win for {self.player2_name}"

    def get_standard_score(self):
        player1_score_name = self.SCORE_NAMES.get(self.player1_score, "")
        player2_score_name = self.SCORE_NAMES.get(self.player2_score, "")
        return f"{player1_score_name}-{player2_score_name}"
