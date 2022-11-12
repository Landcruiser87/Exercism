def score(x, y):
	diam_dict = {
		1 : 10, 
		5 : 5, 
		10: 1
		}

	x_center, y_center = 0, 0
	for rdist, score in diam_dict.items():
		DIST = ((x-x_center)**2 + (y - y_center)**2)**0.5
		if DIST <= rdist:
			return score
	return 0
