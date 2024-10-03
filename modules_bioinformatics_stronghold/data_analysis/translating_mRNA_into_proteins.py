codontab = {
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',    # Serina
    'UUC': 'F', 'UUU': 'F',                            # Fenilalanina
    'UUA': 'L', 'UUG': 'L',                            # Leucina
    'UAC': 'Y', 'UAU': 'Y',                            # Tirosina
    'UAA': '*', 'UAG': '*', 'UGA': '*',                # Stop
    'UGC': 'C', 'UGU': 'C',                            # Cisteina
    'UGG': 'W',                                        # Triptofano
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',    # Leucina
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',    # Prolina
    'CAC': 'H', 'CAU': 'H',                            # Histidina
    'CAA': 'Q', 'CAG': 'Q',                            # Glutamina
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',    # Arginina
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I',                # Isoleucina
    'AUG': 'M',                                        # Methionina
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',    # Treonina
    'AAC': 'N', 'AAU': 'N',                            # Asparagina
    'AAA': 'K', 'AAG': 'K',                            # Lisina
    'AGC': 'S', 'AGU': 'S',                            # Serina
    'AGA': 'R', 'AGG': 'R',                            # Arginina
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',    # Valina
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',    # Alanina
    'GAC': 'D', 'GAU': 'D',                            # Acido Aspartico
    'GAA': 'E', 'GAG': 'E',                            # Acido Glutamico
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G'     # Glicina
}


def translation(seq: str) -> str:
    aa_chain = ""
    for i in range(0, len(seq), 3):
        aa_chain += codontab[seq[i: i + 3]]
    aa_chain = aa_chain.replace("*","")
    return aa_chain
