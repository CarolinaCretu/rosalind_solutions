def find_motif_index(seq, motif):
    index_found = []
    for i in range(0, len(seq)):
        if seq[i: i + len(motif)] == motif:
            index_found.append(i+1)
    return " ".join(str(x) for x in index_found)

