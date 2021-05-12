from collections import defaultdict

class Team:
	def __init__(self, name:str):
		self.name = name
		self.wins = 0
		self.losses = 0
		self.draws = 0
			


	def tally(self, rows):
	

		"""[returns the sum of the rows]

		Args:
			rows ([type]): [description]
		"""	
