class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.losses = 0

    @property
    def played(self):
        return self.wins + self.draws + self.losses

    @property
    def points(self):
        return (self.wins * 3) + self.draws

    def __str__(self):
        return (f"{self.name:30} | "
                f"{self.played:2} | "
                f"{self.wins:2} | "
                f"{self.draws:2} | "
                f"{self.losses	:2} | "
                f"{self.points:2}")


def update_scores(teams, row):
    team_one_name, team_two_name, result = row.split(';')
    team_one = teams.setdefault(team_one_name, Team(team_one_name))
    team_two = teams.setdefault(team_two_name, Team(team_two_name))

    if result == 'win':
        team_one.wins += 1
        team_two.losses += 1
    elif result == 'loss':
        team_one.losses += 1
        team_two.wins += 1
    else:
        team_one.draws += 1
        team_two.draws += 1


def tally(rows):
    results = ["Team                           | MP |  W |  D |  L |  P"]
    if not rows:
        return results

    teams = {}
    [update_scores(teams, row) for row in rows]

    teams = sorted(teams.values(), key=lambda team: (-team.points, team.name))
    results.extend([str(team) for team in teams])
    return results