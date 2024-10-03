from modules_bioinformatics_stronghold.data_manipulation.fasta_files import *
from modules_bioinformatics_stronghold.data_analysis.RNA_splicing import *
from modules_bioinformatics_stronghold.data_analysis.transcribing_DNA_into_mRNA import *
from modules_bioinformatics_stronghold.data_analysis.translating_mRNA_into_proteins import *

given_path = input("path: ")
info_given = readFastaFile(given_path)

dna = RNA_splicing(info_given)
mrna = transcribing_mRNA(dna)
print(translation(mrna))