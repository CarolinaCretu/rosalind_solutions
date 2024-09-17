from modules_bioinformatics_stronghold.data_analysis.transcribing_DNA_into_mRNA import transcribing_mRNA
from modules_bioinformatics_stronghold.data_analysis.translating_mRNA_into_proteins import *
from modules_bioinformatics_stronghold.data_analysis.complementing_DNA import *


def find_start(seq):
    list_start = []
    for i in range(0, len(seq)):
        if seq[i: i+3] == "AUG":
            list_start.append(seq[i:])
    return list_start


def find_stop(seq):
    result = ""
    for i in range(0, len(seq), 3):
        if seq[i: i + 3] == "UAA" or seq[i: i + 3] == "UAG" or seq[i: i + 3] == "UGA":
            result = seq[:i]
            break
    return result


def solution_ORF(seq):
    """
   find the open reading frame given a DNA string 
    """
    # create list of all the possible 6 reading frames
    seq_comp = compliment(seq)
    mrna_1 = transcribing_mRNA(seq_comp)
    mrna_2 = transcribing_mRNA(seq)
    start_1 = find_start(mrna_1)
    start_2 = find_start(mrna_2)
    start_mRNA = []
    start_mRNA += start_1
    for i in start_2:
        if i not in start_mRNA:
            start_mRNA += start_2
    # NOW WE HAVE A LIST OF POSSIBLE READING FRAMES
    lst_ORF = []
    for i in start_mRNA:
        lst_ORF.append(find_stop(i))
    # NOW WE HAVE A LIST OF POSSIBLE READING FRAMES with stop codon taken into account
    for c in lst_ORF:
        if c == '':
            lst_ORF.remove('')
    # WE REMOVED EMPTY ELEMENTS
    lst_no_doubles = []
    for z in lst_ORF:
        if z not in lst_no_doubles:
            lst_no_doubles.append(z)
    # translate remaining open reading frames
    lst_translation = []
    for n in lst_no_doubles:
        lst_translation.append(translation(n))
    return "\n".join(lst_translation)



