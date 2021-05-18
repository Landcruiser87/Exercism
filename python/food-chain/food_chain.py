#This is officially the weirdest one of these i've done yet. 
#I apparently never learned this rhyme.  

ANIMALS = ['fly','spider','bird','cat','dog','goat','cow', 'horse']

VERSE_NEXT_AN = {
				"fly": "I don't know why she swallowed the fly. Perhaps she'll die.",
				"spider": "It wriggled and jiggled and tickled inside her.",
				"bird":"How absurd to swallow a bird!",
				"cat":"Imagine that, to swallow a cat!",
				"dog":"What a hog, to swallow a dog!",
				"goat":"Just opened her throat and swallowed a goat!",
				"cow":"I don't know how she swallowed a cow!",
				"horse":"She's dead, of course!"
				}

def recite(start_verse:int, end_verse:int) -> list:
	"""[Program to generate verses of song]

	Args:
		start_verse (int): [Where to begin]
		end_verse (int): [Where to end]

	Returns:
		list: [A list of the various verses of the song]
	"""
	lyrics = []
	#For iterating through versese
	for i in range(start_verse -1, end_verse): 
		lyrics.append(f"I know an old lady who swallowed a {ANIMALS[i]}.")
		lyrics.append(f'{VERSE_NEXT_AN[ANIMALS[i]]}')
		if i == 7:
			#Janky fix for ending song early when she goes for the horse
			break
			
		if i >= 1:
			x = i
			while x >= 1:
				lyrics.append(f'She swallowed the {ANIMALS[x]} to catch the {ANIMALS[x-1]}.')
				if ANIMALS[x-1] == 'spider':
					
					lyrics[-1] = lyrics[-1:][0][:-1] + " that wriggled and jiggled and tickled inside her."
				x -= 1
			lyrics.append(f"I don't know why she swallowed the fly. Perhaps she'll die.")
		if start_verse != end_verse:
			lyrics.append("")
	if lyrics[-1] == "":
		lyrics.pop()
	return lyrics
		
	#Constraints

	# Always starts with I know an old lady who swalled a {animal}
	# 2nd line varies depending on what it needs to rhyme with
	# Ends wiht "I know why but she swallwed the fly, Perhaps she'll die"

	# Until it reaches the very last where she swallows the horse.  
	# Really weird song. 

# song = print(recite(1, 3))

