def RNA_splicing(dic_info: dict) -> str:
    list_seq = [values for keys, values in dic_info.items()]  # all the introns + RNA seq
    RNA_seq = ""                                              # RNA seq to be modified
    for seq in range(len(list_seq)):
        if len(list_seq[seq]) >= len(RNA_seq):
            RNA_seq = list_seq[seq]                           # found RNA by finding the longest seq
    list_seq.remove(RNA_seq)                                  # remove RNA from list and leave only the introns
    for intron in list_seq:
        RNA_seq = RNA_seq.replace(intron, "", 1)              # remove the introns
    return RNA_seq



