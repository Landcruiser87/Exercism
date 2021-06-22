# https://exercism.io/tracks/python/exercises/tournament/solutions/98dba26693524119ad18ca5d990838aa
# https://exercism.io/tracks/python/exercises/tournament/solutions/06e8b2daa91c4e5fbeae1876e9d0ad7c
# https://exercism.io/tracks/python/exercises/tournament/solutions/cf348e2078e04d5590c7a3315d984ec1
# https://exercism.io/tracks/python/exercises/tournament/solutions/12d6187fd53a4613a57f8f213c1588fa


class Team(object):
	"""[Sets the initial values for each team.  Properties are
	set for MP and P to automatically calculate those values by assigning the
	them to a decorator function.  (think function of a function)]

	Args:
		object ([type]): [description]
	"""	
	def __init__(self, name:str):
		self.name = name
		self.W = 0
		self.L = 0
		self.D = 0
	
	@property
	def MP(self) -> int:
		return self.W + self.D + self.L
	
	@property
	def P(self) -> int:
		return self.W*3 + self.D

def tally(rows:list) -> list:
	"""[This logic processes the team scores]

	Args:
		rows (list): [String inputs for match outcomes]

	Returns:
		list: [Sorted and formated version of team results]
	"""	
	teams = dict()
	for row in rows:
		team1, team2, outcome = row.split(';')
		for name in (team1, team2):
			if name not in teams:
				teams[name] = Team(name)

		if outcome == 'win':
			teams[team1].W += 1
			teams[team2].L += 1
		if outcome == 'loss':
			teams[team1].L += 1
			teams[team2].W += 1
		if outcome == 'draw':
			teams[team1].D += 1
			teams[team2].D += 1

	ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"

	table = sorted(teams.values(), key=lambda x: (-x.P, x.name))
	result = []
	header = ["Team","MP","W","D","L","P"]
	result.append(ROW_FORMAT.format(*header))

	for row in table:
		result.append(ROW_FORMAT.format(
			row.name, 
			row.MP,
			row.W,
			row.D,
			row.L,
			row.P
		))

	return result
