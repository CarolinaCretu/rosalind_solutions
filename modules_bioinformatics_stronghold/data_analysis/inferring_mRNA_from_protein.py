codontab2 = {
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'C': ['TGT', 'TGC'],
    'W': ['TGG'],
    'E': ['GAA', 'GAG'],
    'D': ['GAT', 'GAC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'N': ['AAT', 'AAC'],
    'M': ['ATG'],
    'K': ['AAA', 'AAG'],
    'Y': ['TAT', 'TAC'],
    'I': ['ATT', 'ATC', 'ATA'],
    'Q': ['CAA', 'CAG'],
    'F': ['TTT', 'TTC'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'H': ['CAT', 'CAC'],
    '*': ['UAA', 'UAG', 'UGA']
}


def inferring_mRNA_from_protein(seq: str):
    count = 1
    for aa in seq:
        count = count * len(codontab2[aa])
    count = count * len(codontab2["*"])
    return count % 1_000_000

