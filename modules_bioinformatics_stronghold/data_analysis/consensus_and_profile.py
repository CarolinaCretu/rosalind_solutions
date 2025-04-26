import numpy as np

def consensus(seq_fasta_dic: dict):
   
    for key in seq_fasta_dic:
        n = len(seq_fasta_dic[key]) # number of columns depending on the length of the sequence

    profile_matrix = np.zeros((4, n)) # profile matrix for consensus sequence identification 

    # calculating values from profile matrix
    for key in seq_fasta_dic:
        for i in range(n):
            if seq_fasta_dic[key][i] == "A":
                profile_matrix[0,i] += 1
            elif seq_fasta_dic[key][i] == "C":
                profile_matrix[1,i] += 1
            elif seq_fasta_dic[key][i] == "G":
                profile_matrix[2,i] += 1
            else:
                profile_matrix[3,i] += 1

    # determining consensus sequence
    consensus = ""
    for i in range(n):
        if profile_matrix[0,i] >= profile_matrix[1,i]  and  profile_matrix[0,i] >= profile_matrix[2,i] and profile_matrix[0,i] >= profile_matrix[3,i]:
            consensus += "A"
        elif profile_matrix[1,i] >= profile_matrix[0,i]  and  profile_matrix[1,i] >= profile_matrix[2,i] and profile_matrix[1,i] >= profile_matrix[3,i]:
            consensus += "C"
        elif profile_matrix[2,i] >= profile_matrix[0,i]  and  profile_matrix[2,i] >= profile_matrix[1,i] and profile_matrix[2,i] >= profile_matrix[3,i]:
            consensus += "G"
        else:
            consensus +="T"

    a = profile_matrix[0].astype(int)
    c = profile_matrix[1].astype(int)
    g = profile_matrix[2].astype(int)
    t = profile_matrix[3].astype(int)

    return f"{consensus}\nA: {' '.join(map(str, a))}\nC: {' '.join(map(str, c))}\nG: {' '.join(map(str, g))}\nT: {' '.join(map(str, t))}"

