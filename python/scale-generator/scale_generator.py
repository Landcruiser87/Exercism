SHARPS = ['C', 'a', 'G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
SHARP_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
FLAT_SCALE = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
INTERVAL = {"m":1, "M":2, "A":3}
class Scale:
	"""[This is a function to generate musical key scales]
	"""
	def __init__(self, tonic:str):
		self.tonic = tonic
		if self.tonic in SHARPS:
			self.scale = SHARP_SCALE
		else:
			self.scale = FLAT_SCALE
	def chromatic(self)-> list:
		"""[Function to reorganize the scale with tonic at the root
		or starting position]

		Returns:
			list: [List of the scale with tonic at starting pos]
		"""		
		scale_idx = self.scale.index(self.tonic.capitalize())
		return self.scale[scale_idx:] + self.scale[:scale_idx]

	def interval(self, intervals)-> list:
		"""[Calculates steps of scale]

		Args:
			intervals ([str]): [Shorthand notation for scale progression]

		Returns:
			[type]: [Complete list of musical notes in scale]
		"""		
		chromatic = self.chromatic()
		scale_steps = [INTERVAL[x] for x in intervals]
		if sum(scale_steps) != 12:
			raise ValueError("Incorrect scale generated")
		idx, output = 0, []
		for step in scale_steps:
			output.append(chromatic[idx])
			idx += int(step)
		return output
