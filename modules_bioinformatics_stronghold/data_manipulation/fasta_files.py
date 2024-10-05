def readFastaFile(fasta_path) -> dict:
    """
        Reads Fasta file
        """
    with open(fasta_path, "r") as f:
        fasta_file = [i.strip() for i in f.readlines()]

    fasta_dict = {}  # dictionary for labels + data
    fasta_label = ""  # string for holding the current label

    for line in fasta_file:
        if ">" in line:
            fasta_label = line
            fasta_dict[fasta_label] = ""
        else:
            fasta_dict[fasta_label] += line
    return fasta_dict


