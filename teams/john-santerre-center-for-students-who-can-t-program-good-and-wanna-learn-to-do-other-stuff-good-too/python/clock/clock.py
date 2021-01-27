class Clock:
	def __init__(self, hour: int, minute: int):
		"""[Clock initialization]

		Args:
			hour (int): [Hour of the clock]
			minute (int): [Minute of the clock]
		"""	
		self._hour = (hour + minute // 60) % 24
		self._minute = minute % 60
	
	#Use .format to format time correctly
	def __repr__(self) -> str:
		return '{:02d}:{:02d}'.format(self._hour, self._minute)
	
	# Makes sure both components of time is equal
	def __eq__(self, other) -> bool:
		return self._hour == other._hour and self._minute == other._minute
	
	# By reinstantiating class, formats time to add minutes
	def __add__(self, minutes: int) -> str:
		return Clock(self._hour, self._minute + minutes)

	# By reinstantiating class, formats time to subtract minutes
	def __sub__(self, minutes: int) -> str:
		return Clock(self._hour, self._minute - minutes)
