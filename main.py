from modules_bioinformatics_stronghold.data_manipulation.fasta_files import *
from modules_bioinformatics_stronghold.data_analysis.consensus_and_profile import *

if __name__ == "__main__":

    given_path = input("path: ")
    info_given = readFastaFile(given_path)
    print(consensus(info_given))
