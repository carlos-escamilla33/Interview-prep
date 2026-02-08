def helper(word):
    ht = {}

    for char in word:
        if char not in ht:
            ht[char] = 0
        ht[char] += 1
    
    return ht

def closeStrings(word1, word2):
    # check the length
    if len(word1) != len(word2):
        return False
    
    word1_ht = helper(word1)
    word2_ht = helper(word2)

    # check the characters are the same and the frequency of each character
    return (word1_ht.keys() == word2_ht.keys() 
            and sorted(word1_ht.values()) == sorted(word2_ht))


# space - O(n)
# runtime - O(nlogn)
