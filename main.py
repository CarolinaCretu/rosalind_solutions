from modules_bioinformatics_stronghold.data_manipulation.simple_file import *
from modules_bioinformatics_stronghold.data_analysis.calculating_protein_mass import *

given_path = input("path: ")
info_given = readFileSimple(given_path)


print(calculating_protein_mass(info_given))