class BowlingGame:
	'''
	This is a class to calculate a bowling score. 
	'''
	def __init__(self):
		self._roll = []
	
	def roll(self, pins:int):
		"""[This method takes in one throw and validates it.
		Also contains logic to navigate the 10th Frame]

		Args:
			pins (int): [Num of pins knocked down]
		"""
		#Checks individual pins to make sure range is correct
		if pins < 0 or pins > 10:
			raise ValueError('You sit on a throne of lies!  aka. Wrong amount of pins in roll')

		#Count the throws
		_numrolls = len(self._roll)

		def determineBonus(pins:int, _numrolls:int) -> int:
			"""[Determines 10th Frame Bonus]

			Args:
				pins (int): [current roll]
				_numrolls (int): [index of current roll]

			Returns:
				int: [bonus frames]
			"""
			_bonus = 0
			#If 10.1 is a strike
			if self._roll[_numrolls - 2] == 10:
				#10.2 + 10.3 can't be greater than 10 or 10.2 needs a strike
				if (self._roll[_numrolls - 1] + pins) <= 10 or self._roll[_numrolls - 1] == 10:
					_bonus += 2
				else:
					raise ValueError('Last two frames of Match don\'t add up to 10')
			#If 10.2 is a strike
			elif self._roll[_numrolls - 1] == 10:
				_bonus += 2
			#If 10.1 + 10.2 is spare
			elif self._roll[_numrolls - 2] + self._roll[_numrolls - 1]  == 10:
				_bonus += 1
			
			return _bonus

		# #Stupid single test failure check.  Doesn't work
		# if _numrolls == 1 and sum(self._rolls) > 10:
		# 	raise ValueError('Can\'t have more than 10 pins in one frame')
		
		#10th Frame check
		if _numrolls == 20:										 
			_bonus = determineBonus(pins, _numrolls)
			if _bonus > 0:
				self._roll.append(pins)
			else:
				raise ValueError('No bonus ball without a strike or spare')

		elif _numrolls >= 21:
			raise ValueError('10 frames only!  No soup for you!')

		else:
			self._roll.append(pins)

		#10th Logic
		# 18th throw is the first throw of the 10th frame
		# no matter what they advance to the 19th
		# Do eval from 20th (That way 18 and 19 are always evaluated)
			# If frame 18 is strike = 2 x bonus ball
			# If frame 19 is strike = bonus ball
			# If frame 19 is spare = bonus ball
			# If frame >= 21 = game over

	def score(self) -> int:
		"""[Determines type of score and adds to total score]
		Functions for each outcome
		"""
		_score = 0
		_frameidx = 0
		def frameSum():
			return self._roll[_frameidx] + self._roll[_frameidx + 1]

		def isSpare():
			return self._roll[_frameidx] + self._roll[_frameidx + 1] == 10

		def isStrike():
			return self._roll[_frameidx] == 10

		def strikeBonus():
			return self._roll[_frameidx + 1] + self._roll[_frameidx + 2]

		def spareBonus():
			return self._roll[_frameidx + 2]
		
		for frame in range(10):
			if isStrike():
				_score += 10 + strikeBonus()
				_frameidx += 1

			elif isSpare():
				_score += 10 + spareBonus()
				_frameidx += 2

			else:
				_score += frameSum()
				_frameidx += 2

		return _score
