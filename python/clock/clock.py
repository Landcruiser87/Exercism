class Clock:
	def __init__(self, hour, minute):

		self.hour = hour
		self.minute = minute

	def __repr__(self):
		return 

	def __eq__(self, other):
		pass

	def __add__(self, minutes):
		pass

	def __sub__(self, minutes):
		pass



import unittest

class ClockTest(unittest.TestCase):
	# Create A New Clock With An Initial Time
	def test_on_the_hour(self):
		self.assertEqual(str(Clock(8, 0)), "08:00")

	def test_add_minutes(self):
		self.assertEqual(str(Clock(10, 0) + 3), "10:03")

	def test_subtract_minutes(self):
		self.assertEqual(str(Clock(10, 3) - 3), "10:00")

	def test_clocks_with_same_time(self):
		self.assertEqual(Clock(15, 37), Clock(15, 37))






if __name__ == "__main__":
	unittest.main()
