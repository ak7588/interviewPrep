"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.
"""

def isAlienSorted(self, words: List[str], order: str) -> bool:
    alphabet = {}
    for ind, char in enumerate(order):
        alphabet[char] = ind
    for i in range(len(words)-1):
        for j in range(len(words[i])):
            if j >= len(words[i+1]):
                return False
            if words[i][j] != words[i+1][j]:
                if alphabet[words[i][j]] > alphabet[words[i+1][j]]:
                    return False
                break
    return True
    
      
