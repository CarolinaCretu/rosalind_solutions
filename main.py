from modules_bioinformatics_stronghold.data_manipulation.simple_file import *
from modules_bioinformatics_stronghold.data_analysis.inferring_mRNA_from_protein import *

given_path = input("path: ")
info_given = readFileSimple(given_path)


print(inferring_mRNA_from_protein(info_given))