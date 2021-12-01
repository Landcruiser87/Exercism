class Allergies:

	def __init__(self, score:int):
		"""[Var setup]

		Args:
			score ([int]): [Allergy score to eval]
		"""		
		self._score = score
		self.list = []
		self.allergens = {
			'eggs': 1,
			'peanuts': 2,
			'shellfish': 4,
			'strawberries': 8,
			'tomatoes': 16,
			'chocolate': 32,
			'pollen': 64, 
			'cats': 128
		}

	def allergic_to(self, item:str) -> bool:
		"""[Determines if person is allergic to item in allergens dict.  If bitwise comparison of both match, return True]  

		Args:
			item ([str]): [Allergen]

		Returns:
			[bool]: [True if allergic, False if not]
		"""		
		if self._score & self.allergens[item]:
			return True
		else:
			return False

	@property
	def lst(self)->list:
		"""[aggregates list of possible allergens.  If allergens score lookup and score bitwise comparison match, appends value to return list]

		Returns:
			[list]: [List of possible allergens]
		"""		
		for key, score in self.allergens.items():
			if self._score & score:
				self.list.append(key)
		return self.list
