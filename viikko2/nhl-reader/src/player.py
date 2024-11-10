class Player:
    def __init__(self, data):
        self.name = data['name']
        self.nationality = data['nationality']
        self.assists = data['assists']
        self.goals = data['goals']
        self.team = data['team']
    
    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {self.goals + self.assists}"
