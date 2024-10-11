from modules_bioinformatics_stronghold.data_manipulation.simple_file import *
from modules_bioinformatics_stronghold.data_analysis.enumerating_gene_orders import *

if __name__ == "__main__":

    given_path = input("path: ")
    info_given = readFileSimple(given_path)
    print(enumerating_gene_orders(info_given))
