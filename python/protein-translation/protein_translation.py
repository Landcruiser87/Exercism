protein_dict = {"Methionine": ["AUG"],
	 "Phenylalanine": ["UUU", "UUC"],
	 "Leucine": ["UUA", "UUG"],
	 "Serine": ["UCU", "UCC", "UCA", "UCG"],
	 "Tyrosine": ["UAU", "UAC"],
	 "Cysteine": ["UGU", "UGC"],
	 "Tryptophan": ["UGG"],
	 "STOP": ["UAA", "UAG", "UGA"]}

def proteins(strand):
	codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
	proteins = []
	for codon in codons:
		for key, val in protein_dict.items():
			if codon in val:
				if key == "STOP":
					return proteins
				else:
					proteins.append(key)
	return proteins
