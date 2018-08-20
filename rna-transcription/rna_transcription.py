def to_rna(dna_strand):
    '''
    Given a DNA strand, return its RNA complement
    '''

    transcript={'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna=[]

    for x in dna_strand.upper():
        if x not in transcript:
            raise Exception("Meaningful message indicating the source of the error")

    for x in dna_strand.upper():
        rna.append(transcript.get(x))

    return ''.join(rna)
