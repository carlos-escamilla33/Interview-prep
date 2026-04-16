
def groupAnagrams(strs):
    anagram_ht = {}

    for word in strs:
        sortedWord = tuple(sorted(word))

        if sortedWord not in anagram_ht:
            anagram_ht[sortedWord] = []
        anagram_ht[sortedWord].append(word)
    
    res = []

    for val in anagram_ht.values():
        res.append(val)
    
    return res