#Alex Tol, Mathew Jones
from random import randint
import re

bases = ['A','G','T','C']
#a and c require different nucleotides
def Mutate(DNASeq,Mut,n=None):
    #choose which mutation
    if(Mut == 'M'):
        return Missense(DNASeq)
    elif(Mut == 'N'):
        return Nonesense(DNASeq)
    elif(Mut == 'I'):
        return Insertion(DNASeq)
    elif(Mut == 'D'):
        return Deletion(DNASeq)
    elif(Mut == 'U'):
        return Duplication(DNASeq)
    elif(Mut == 'R'):
        return Repeat(DNASeq)
        
def Missense(DNASeq):
    mutSpace = randint(0,len(DNASeq)-1)

    newSeq = ''
    space = 0
    for each nuc in DNASeq:
        if(space != mutSpace):
            newSeq = newSeq + nuc
        else:
            newNuc = DNASeq[mutSpace]
            while(newNuc == DNASeq[mutSpace]):
                newNuc = bases[randint(0,3)]
            newSeq = newSeq + newNuc

    return newSeq

def NonSense(DNASeq):
    locations = []
    regex = re.compile('AG')
    
    for m in rege.finditer(DNASeq):
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
    return DNASeq[:space] + DNASeq[space+1:]

def Duplication(DNASeq,n):
    mutSpace = randint(0,len(DNASeq)-1)

    newString = ''
    if(n+1 > len(DNASeq)+1):
        newString = DNASeq[mutSpace:]
    else:
        newString = DNASeq[mutSpace:mutSpace+n+1]

    return DNASeq[:mutSpace+n+1] + newString + DNASeq[mutSpace+n+1:]

def Repeat(DNASeq,n):
    mutSpace = randint(0,len(DNASeq)-1)

    newString = ''
    if(n+1 > len(DNASeq)+1):
        newString = DNASeq[mutSpace:]
    else:
        newString = DNASeq[mutSpace:mutSpace+n+1]

    NewSeq = ''
    NewSeq = DNASeq[:mutSpace+n+1]

    for i in range(0,n):
        NewSeq = NewSeq + newString
    
    return NewSeq + DNASeq[mutSpace+n+1:]