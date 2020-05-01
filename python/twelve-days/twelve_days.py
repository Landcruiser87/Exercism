def verse(number):
	nums = ['first',
			'second',
			'third',
			'fourth',
			'fifth',
			'sixth',
			'seventh',
			'eighth',
			'ninth',
			'tenth',
			'eleventh',
			'twelfth']
	
	lyrics = [
		"twelve Drummers Drumming, ",
		"eleven Pipers Piping, ",
		"ten Lords-a-Leaping, ",
		"nine Ladies Dancing, ",
		"eight Maids-a-Milking, ",
		"seven Swans-a-Swimming, ",
		"six Geese-a-Laying, ",
		"five Gold Rings, ",
		"four Calling Birds, ",
		"three French Hens, ",
		"two Turtle Doves, ",
		"and a Partridge in a Pear Tree."]
	lyrics_cnt = len(lyrics)
	output = "On the {} day of Christmas my true love gave to me: ".format(nums[number-1])

	if number == 1:
		output = "{}{}".format(output,'a Partridge in a Pear Tree.')
	else:
		output = "{}{}".format(output,"".join([lyrics[idx] for idx in range(lyrics_cnt - number, lyrics_cnt)]))
		
	return output

def recite(start_lyrics, end_lyrics):
	output = [verse(x) for x in range(start_lyrics, end_lyrics + 1)]
	return output

