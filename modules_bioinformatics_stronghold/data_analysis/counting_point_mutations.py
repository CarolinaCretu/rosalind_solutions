def count_point_mutation(seq_list):
    count = 0
    for i in range(len(seq_list[0])):
        if seq_list[0][i] != seq_list[1][i]:
            count += 1
    return count

