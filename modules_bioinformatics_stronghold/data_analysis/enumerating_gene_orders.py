import itertools


def enumerating_gene_orders(number):
    elements = []
    for i in range(int(number)):
        elements.append(i+1)
    possibilities = list(itertools.permutations(elements, int(number)))
    print(len(possibilities))
    for x in possibilities:
        print(" ".join([str(i) for i in x]))



