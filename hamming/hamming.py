def distance(strand_a, strand_b):

    """
    Based on two passed equal DNA strands calculates the Hamming distance for them.
    """

    if len(strand_a) != len(strand_b) or not strand_a.isalpha() or not strand_b.isalpha():
        raise Exception("Provided strands aren't equal or aren't DNA strands. Please provide equal strands of equal length in order to calculate the Hamming distance.")

    sum = 0
    for i, letter in enumerate(strand_a):
        if strand_b[i] != letter:
            sum+=1

    return sum
