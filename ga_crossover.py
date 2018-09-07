import sys
print(sys.version)

"""
Authors:
Matthew Jones
Alex Tol
"""
import random

def generate_random_num(lower, upper):
    """
    Function that generates a random number between the two numbers passed inclusively

    Args:
        lower (int): lower bound
        upper (int): upper bound

    Return:
        int: a random number between lower and upper

    Examples:
        >>generate_random_num(1, 5)
        >>5
    """
    return random.randint(lower, upper)

def generate_random_nucleotide(nucleotide_letter):
    """
    This function generates a random nucleotide based on the given letter

    Args:
        nucleotide_letter (str): Based on this value one value will be returned at random

    Return:
        str: A letter according to the rules of specific nucleotides 

    Examples:
        >>generate_random_nucleotide('R')
        >>'A'
        >>generate_random_nucleotide('Y')
        >>'C'
    """

    even_general_chance = generate_random_num(0,3)
    outcome = even_general_chance % 2

    odd_general_chance = generate_random_num(0,2)

    if (nucleotide_letter == 'R'): # A or G
        if (outcome == 0):
            return 'A'
        else:
            return 'G'
    elif (nucleotide_letter == 'Y'): # C or T
        if (outcome == 0):
            return 'C'
        else:
            return 'T'
    elif (nucleotide_letter == 'N'): # Any 
        if (even_general_chance == 0):
            return 'A'
        elif (even_general_chance == 1):
            return 'G'
        elif (even_general_chance == 2):
            return 'C'
        else:
            return 'T'
    elif (nucleotide_letter == 'W'): # Weak A or T
        if (outcome == 0):
            return 'A'
        else:
            return 'T'
    elif (nucleotide_letter == 'S'): # String G or C
        if (outcome == 0):
            return 'G'
        else:
            return 'C'
    elif (nucleotide_letter == 'M'): # Amino A or C
        if (outcome == 0):
            return 'A'
        else:
            return 'C'
    elif (nucleotide_letter == 'K'): # Keto G or T
        if (outcome == 0):
            return 'G'
        else:
            return 'T'
    elif (nucleotide_letter == 'B'): # B Not A
        if (odd_general_chance == 0):
            return 'C'
        elif (odd_general_chance == 1):
            return 'G'
        else:
            return 'T'
    elif (nucleotide_letter == 'H'): # H Not G
        if (odd_general_chance == 0):
            return 'A'
        elif (odd_general_chance == 1):
            return 'C'
        else:
            return 'T'
    elif (nucleotide_letter == 'D'): # D Not C
        if (odd_general_chance == 0):
            return 'A'
        elif (odd_general_chance == 1):
            return 'G'
        else:
            return 'T'
    elif (nucleotide_letter == 'V'): # V Not T
        if (odd_general_chance == 0):
            return 'A'
        elif (odd_general_chance == 1):
            return 'G'
        else:
            return 'C'
    else:
        return 'Ack! Unpredicted value!'


def generate_nucleotide_preprocessing_map():
    """
    This function generates a python dictionary that acts like a map
    for use in inverting nucleotide sequences 

    Returns:
        dict: a dictionary with all possible nucleotide values outside of the usual base to be mapped to the bases
    """

    c_or_t = generate_random_nucleotide('Y')
    a_or_g = generate_random_nucleotide('R')
    any_nuc = generate_random_nucleotide('N')
    weak = generate_random_nucleotide('W')
    strong = generate_random_nucleotide('S')
    amino = generate_random_nucleotide('M')
    keto = generate_random_nucleotide('K')
    not_a = generate_random_nucleotide('B')
    not_g = generate_random_nucleotide('H')
    not_c = generate_random_nucleotide('D')
    not_t = generate_random_nucleotide('V')

    processing_map = {
                    'Y': c_or_t, 'R': a_or_g, 
                    'N': any_nuc, 'W': weak, 'S': strong,
                    'M': amino, 'K': keto, 'B': not_a, 
                    'H': not_g, 'D': not_c, 'V': not_t,
                    'G': 'G', 'C': 'C', 'T': 'T', 'A': 'A'
    }

    return processing_map


def crossover(dna):
    """
    Takes in one row of the dna seqence file
    and generates the complementary nucleotide strand to the privded DNA 
    sequence. Then randomly selects a location to start the crossover and
    randomly select the length of the DNA sequence to crossover and outputs a 
    tuple containing the original DNA sequence with the crossover as well as 
    an integer representing the location and the length of the crossover

    Args:
        dna (str): a sequence of length n 

    Returns:
        tuple: contains an original sequence with the crossover, location of 
               start of the crossover, and the length of the crossover

    Example: 
        >>crossover("GCGGCCCAGGCCCGGAACCTTCCCTGGTC")
        >>("GCGGGGGTCGCCCGGAACCTTCCCTGGTC", 4, 5)
    """
    # Preprocess the list initially converting the nucleotides outside of the 
    # original four to inside the base four
    preprocessing_dna_list = list(dna)
    preprocessing_map = generate_nucleotide_preprocessing_map()
    dna_sequence_list = [preprocessing_map.get(item) for item in preprocessing_dna_list]

    # produce a list of inversed values based off of the dna sequence
    inverse_map = {
                    'G':'C', 'C':'G', 'A':'T', 'T':'A'
    }
    inv_dna_list = [inverse_map.get(item) for item in dna_sequence_list]
    
    # generate the indicies and the length of the crossover
    crossover_start = generate_random_num(0, len(dna_sequence_list) - 1)
    len_of_crossover = generate_random_num(0, len(dna_sequence_list) - 1)
    
    # assign these cuts to dummy variables
    dna_crossover = dna_sequence_list[crossover_start:len_of_crossover]
    inv_dna_crossover = inv_dna_list[crossover_start:len_of_crossover]
    
    # place these cuts in the opposing sections of the opposite sequence
    dna_sequence_list[crossover_start:len_of_crossover] = inv_dna_crossover
    inv_dna_list[crossover_start:len_of_crossover] = dna_crossover
    
    # generate a string from the list 
    dna_string = ''.join(dna_sequence_list) 
    
    return (dna_string, crossover_start, len_of_crossover)

def main():
    """
    Starts the main sequence of operations
    """

    fname = "dna_sequences.dat"
    to_write_to = open('crossover_results.dat', 'w+')
    f = open(fname, 'r')
    for line in f:
        crossover_result = crossover(str(line).rstrip())
        formatted_string = '({},{},{}),'.format(crossover_result[0], crossover_result[1], crossover_result[2])
        to_write_to.write(formatted_string)
            
    f.close()
    to_write_to.close()

def crossover_test():
    test_val = "GCGGCCCAGGCCCGGAACCTTCCCTGGTCGTGCGCCATATGTAAGGCCAGCCGCGGCAGGACCAAGGCGG"
    result_val = crossover(test_val)
