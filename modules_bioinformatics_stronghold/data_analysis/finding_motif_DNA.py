def find_motif_index(seq: str, motif: str) -> str:
    index_found = []
    for i in range(0, len(seq)):
        if seq[i: i + len(motif)] == motif:
            index_found.append(i+1)
    return " ".join(str(x) for x in index_found)

