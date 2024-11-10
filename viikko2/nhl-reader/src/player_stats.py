class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()
        best_players = [player for player in players if player.nationality == nationality]
        best_players.sort(key=lambda player: -(player.goals + player.assists))
        return best_players
