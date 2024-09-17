from modules_bioinformatics_stronghold.data_manipulation.fasta_files import *
from modules_bioinformatics_stronghold.data_analysis.open_reading_frame import *

given_path = input("path: ")
info_given = readFastaFile(given_path)

for keys, values in info_given.items():
    print(solution_ORF(values))
