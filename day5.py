from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()
    

def scan(polymer: str) -> str:
    if any([same_type(pair[0], pair[1]) and pair[0] != pair[1] for pair in pairs(polymer)]):
        return alchreduce(polymer)
    else:
        return polymer
    

def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            # if we have run through all the pairs
            # complete reaction and scan for other reactive monomers
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            return scan(reduced)
              
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            to_delete.add(pair[2]+1)
            # once a reacting monomer tuple is identified
            # react them and check if any remaining reactive monomers
            # are in the resulting sequence
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)    
            return scan(reduced)
           
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"


#print(alchreduce(TEST))


with open('C:/Python/projects/adventofcode/data/polymer.txt') as f:
    #polymer = [line.strip() for line in f]
    polymer = f.read()


alchreduce(polymer)
