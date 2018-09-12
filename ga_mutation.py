#Alex Tol, Mathew Jones
from random import randint
import re

bases = ['A','G','T','C']
mutations = ['M','N','I','D','U','R']

def main():
    fname = "dna_sequences.dat"
    to_write_to = open('mutation_results.dat', 'w+')
    f = open(fname, 'r')

    for line in f:
        mutation = mutations[randint(0,5)]
        result = None
        if(mutation == 'U' or mutation == 'R'):
            n = randint(1,10)
            result = Mutate(line,mutation,n)
        else:
            result = Mutate(line,mutation)

        output = mutation + '\n' + result
        to_write_to.write(output)

#a and c require different nucleotides
def Mutate(DNASeq,Mut,n=None):
    #choose which mutation
    if(Mut == 'M'):
        return Missense(DNASeq)
    elif(Mut == 'N'):
        return NonSense(DNASeq)
    elif(Mut == 'I'):
        return Insertion(DNASeq)
    elif(Mut == 'D'):
        return Deletion(DNASeq)
    elif(Mut == 'U'):
        return Duplication(DNASeq,n)
    elif(Mut == 'R'):
        return Repeat(DNASeq,n)
        
def Missense(DNASeq):
    mutSpace = randint(0,len(DNASeq)-1)

    newSeq = ''
    space = 0
    for nuc in DNASeq:
        if(space != mutSpace):
            newSeq = newSeq + nuc
        else:
            newNuc = DNASeq[mutSpace]
            while(newNuc == DNASeq[mutSpace]):
                newNuc = bases[randint(0,3)]
            newSeq = newSeq + newNuc
        space = space + 1

    return newSeq

def NonSense(DNASeq):
    locations = []
    regex = re.compile('AG')
    
    for m in regex.finditer(DNASeq):
        locations.append(m.start())

    if(len(locations) == 0):
        return DNASeq
    else:
        space = locations[randint(0,len(locations)-1)] - 1
        return DNASeq[:space] + 'T' + DNASeq[space+1:]

def Insertion(DNASeq):
    newNuc = bases[randint(0,3)]
    mutSpace = randint(0,len(DNASeq)-1)
    
    return DNASeq[:mutSpace] + newNuc + DNASeq[mutSpace:]

def Deletion(DNASeq):
    mutSpace = randint(0,len(DNASeq)-1)
    return DNASeq[:mutSpace] + DNASeq[mutSpace+1:]

def Duplication(DNASeq,n):
    mutSpace = randint(0,len(DNASeq)-1)

    newString = ''
    if(n+1 > len(DNASeq)+1):
        newString = DNASeq[mutSpace-1:]
    else:
        newString = DNASeq[mutSpace:mutSpace+n]
    #print(mutSpace)
    #print(newString)
    return DNASeq[:mutSpace+n].rstrip() + newString.rstrip() + DNASeq[mutSpace+n:].rstrip() + '\n'

def Repeat(DNASeq,n):
    mutSpace = randint(0,len(DNASeq)-1)

    newString = ''
    if(n+1 > len(DNASeq)+1):
        newString = DNASeq[mutSpace-1:]
    else:
        newString = DNASeq[mutSpace:mutSpace+n]

    NewSeq = ''
    NewSeq = DNASeq[:mutSpace+n].rstrip()

    for i in range(0,n):
        NewSeq = NewSeq.rstrip() + newString.rstrip()
    
    #print(mutSpace)
    #print(newString)
    return NewSeq.rstrip() + DNASeq[mutSpace+n:].rstrip() + '\n'