def to_rna(dna_strand):
    switch_dict = {
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U"
    }
    rna = []
    for char in dna_strand:
        if char in switch_dict.keys():
            rna.append(switch_dict[char])
        else:
            rna.append(char)
    return "".join(rna)
    