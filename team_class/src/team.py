class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        self.injured = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        return (True if player in self.players else False)
        # return player in self.players  --- even nicer solution

    def play_game(self, won_or_not):
        if won_or_not: 
            self.points += 3
        else:
            self.points += 0
    
    def players_injured(self, players):
        self.injured += len(players)