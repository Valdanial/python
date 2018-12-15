def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Impossible to compare two DNA strands with different lengths")
    distance = 0
    index = 0
    for item in strand_a:
        if item != strand_b[index]:
            distance += 1
        index += 1
    return distance
