class BowlingGame:
	'''
	This is a class to calculate a bowling score. 
	'''
	def __init__(self):
		self._roll = []

	def roll(self, pins:int):
		"""[This method takes in one throw and validates it]

		Args:
			pins (int): [Num of pins knocked down]
		"""
		#Checks individual pins to make sure range is correct
		if pins < 0 or pins > 10:
			raise ValueError('You sit on a throne of lies!  aka. Wrong amount of pins in roll')
		
		#Count the throws
		_numrolls = len(self._roll)
		def isEqualten(x):
			return x == 10
		#10th Frame check
		if _numrolls == 19:													 
			if self._roll[-1] == 10 or pins == 10 or (self._roll[-1] + pins) == 10:
				self._roll.append(pins)
			else:
				raise ValueError('No bonus ball without a strike or spare')
		elif _numrolls == 20:
			if self._roll[-1] + pins < 10 or (self._roll[-1] + self._roll[-2]) == 10:
				self._roll.append(pins)
			else:
				raise ValueError('No bonus ball without a strike or spare')

		elif _numrolls >= 21:
			if self._roll[-1] ==  0 or self._roll[-2] == 0:
				raise ValueError('10 frames only!  No soup for you!')
		else:
			self._roll.append(pins)

		#10th Logic
		# 18th throw is the first throw of the 10th frame
		# no matter what they advance to the 19th
		# Do eval from 19th
			# If frame 18 is strike = 2 x bonus ball
			# If frame 19 is strike = bonus ball
			# If frame 19 is spare = bonus ball
			#
			# If frame 20 is strike or spare = bonus ball
			# If frame 20 + frame 19 != 20, game over

		# self._roll.append(pins)

	def score(self) -> int:
		"""[Determines type of score and adds to total score]
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
			

import unittest

# # Tests adapted from `problem-specifications//canonical-data.json`

class BowlingTest(unittest.TestCase):
	def roll_new_game(self, rolls):
		game = BowlingGame()
		for roll in rolls:
			game.roll(roll)
		return game
	def test_a_strike_in_the_last_frame_gets_a_two_roll_bonus_that_is_counted_once(self):
		rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 1]
		game = self.roll_new_game(rolls)
		self.assertEqual(game.score(), 18)

	def test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self):
		rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]
		game = self.roll_new_game(rolls)
		self.assertEqual(game.score(), 90)

	def test_cannot_roll_after_bonus_roll_for_spare(self):
		rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 2]
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(2)
	
	def test_cannot_roll_after_bonus_rolls_for_strike(self):
		rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 2]
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(2)
	#! Failtown
	def test_cannot_roll_if_game_already_has_ten_frames(self):
		rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(0)

	def test_rolls_cannot_score_negative_points(self):
		rolls = []
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(-1)

	#! Failtown
	def test_the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike(self):
		rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(10)
	#! Failtown
	def test_two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points(self):
		rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5]
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(6)
	#! Failtown
	def test_two_rolls_in_a_frame_cannot_score_more_than_10_points(self):
		rolls = [5]
		game = self.roll_new_game(rolls)
		with self.assertRaisesWithMessage(Exception):
			game.roll(6)

	def assertRaisesWithMessage(self, exception):
		return self.assertRaisesRegex(exception, r".+")
	
if __name__ == "__main__":
	unittest.main()
