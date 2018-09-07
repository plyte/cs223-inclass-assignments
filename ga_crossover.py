import sys
print(sys.version)

"""
Authors:
Matthew Jones
Alex Tol
"""
import random

def generate_random_num(lower, upper):
    return random.randint(lower, upper)

def crossover(dna):
    """
    Takes in one row of the dna seqence file
    and generates the complementary nucleotide strand to the privded DNA 
    sequence. Then randomly selects a location to start the crossover and
    randomly select the length of the DNA sequence to crossover

    Example: 
        >>crossover("GCGGCCCAGGCCCGGAACCTTCCCTGGTC")
        >>"CGCCGGGTCCGGGCCTTGGAAGGACCAG"
    """
    dna_sequence_list = list(dna)
    inverse_map = {'G':'C', 'C':'G', 'A':'T', 'T':'A'}
    inv_dna_list = [inverse_map.get(item) for item in dna_sequence_list]
    
    crossover_start = generate_random_num(0, len(inv_dna_list) - 1)
    len_of_crossover = generate_random_num(0, len(inv_dna_list) - 1)
    
    print('length of the dna sequence: {}'.format(len(dna)))
    print('index to start at: {}'.format(crossover_start))
    print('length of the crossover is: {}'.format(len_of_crossover))
    
    dna_crossover = dna_sequence_list[crossover_start:len_of_crossover]
    inv_dna_crossover = inv_dna_list[crossover_start:len_of_crossover]
    
    dna_sequence_list[crossover_start:len_of_crossover] = inv_dna_crossover
    inv_dna_list[crossover_start:len_of_crossover] = dna_crossover
    
    print(type(dna_sequence_list))
    print(type(inv_dna_list))
    
    print(dna_sequence_list)
    print(inv_dna_list)
    dna_string = ''.join(dna_sequence_list)
    inv_dna_string = ''.join(inv_dna_list)
    print(dna_string)
    print(inv_dna_string)
    
    
    return (dna_string, inv_dna_string)

def crossover_test():
    test_val = "GCGGCCCAGGCCCGGAACCTTCCCTGGTCGTGCGCCATATGTAAGGCCAGCCGCGGCAGGACCAAGGCGG"
    result_val = crossover(test_val)
    print(result_val)

if __name__ == "__main__":
    fname = "dna_sequences.dat"
    to_write_to = open('crossover_results.dat', 'w+')
    with open(fname, 'r') as f:
        content = f.readline()
        print(content)
        crossover_result = crossover(str(content).rstrip())
        to_write_to.write(crossover_result)
        while content:
            content = f.readline()
            crossover_result = crossover(content)
            to_write_to.write(crossover_result)
            
        f.close()
        
    to_write_to.close()
