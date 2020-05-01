def latest(scores):
	return scores[-1]


def personal_best(scores):
	return max(scores)


def personal_top_three(scores):
	score_sort = sorted(scores, reverse=True)
	return score_sort[0:3]