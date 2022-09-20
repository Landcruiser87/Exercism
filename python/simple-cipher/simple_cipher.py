import secrets
from string import ascii_lowercase
from itertools import cycle
class Cipher:
	def __init__(self, key=None):
		if key is None:
			self.key = self._random_key()
		else:
			self.key = key
			if not self.key.isalpha():
				raise ValueError("Key must be only letters")
			
			self.key = self.key.lower()
		
		self.LETTER_DICT = {x: idx for idx, x in enumerate(ascii_lowercase)}

	def _random_key(self):
		return ''.join(secrets.choice(ascii_lowercase) for _ in range(100))

	def encode(self, text):
		encoded_text = ""
		for key_let, letter in zip(cycle(self.key), text):
			encoded_text += ascii_lowercase[(self.LETTER_DICT[letter] + self.LETTER_DICT[key_let]) % 26]
		return encoded_text
	
	def decode(self, text):
		decoded_text = ""
		for key_let, letter in zip(cycle(self.key), text):
			decoded_text += ascii_lowercase[(self.LETTER_DICT[letter] - self.LETTER_DICT[key_let]) % 26]
		return decoded_text

