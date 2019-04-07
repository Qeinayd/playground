# https://www.codewars.com/kata/complementary-dna/

def DNA_strand(dna):
    dna = list(dna)
    compl = {
        'T': 'A', 'A': 'T',
        'C': 'G', 'G': 'C'
    }
    
    for i in range(len(dna)):
        dna[i] = compl.get(dna[i])
        
    return ''.join(dna)
