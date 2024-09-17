complimentary_nuc = {"A": "T", "C": "G", "G": "C", "T": "A"}


def compliment(seq):
    compliment_not_rev = ""
    for i in seq:
        compliment_not_rev += complimentary_nuc[i]
    return compliment_not_rev[::-1]


