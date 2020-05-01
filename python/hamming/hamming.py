def distance(strand_a, strand_b):
	if len(strand_a) != len(strand_b):
		raise ValueError("YER STRANDS ARE UNEQUAL LADDY")

	cntr = 0

	for idx in range(len(strand_a)):
		if strand_a[idx] != strand_b[idx]:
			cntr += 1
	
	return cntr

	

