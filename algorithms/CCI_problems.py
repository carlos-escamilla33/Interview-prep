
# Implement an algorithm to determine if a string has all unique characters
# What if you can't use a data structure

def isUnique(s):
    charSet = {}

    for letter in s:
        if letter in charSet:
            return False
        else:
            charSet[letter] = True
    
    return True

# print(isUnique("adf"))

# Given two strings, write a method to decide if one is a permutation of the other.

def frequencyCounter(s):
    strCount = {}

    for l in s:
        if l not in strCount:
            strCount[l] = 1
        else:
            strCount[l]+=1
    
    return strCount

def isPermutation1(s1, s2):
    s1Dict = frequencyCounter(s1)
    s2Dict = frequencyCounter(s2)

    for l in s2Dict:
        if l not in s1Dict or s2Dict[l] != s1Dict[l]:
            return False
        else:
            s1Dict[l]-=1
            s2Dict[l]-=1                                        
    
    return True

# print(isPermutation("ABC", "CABA"))

def isPermutation(s1, s2):
    charCounts = 128 * [0]
    
    for letter in s1:
        asciiVal = ord(letter)
        charCounts[asciiVal]+=1
    
    for letter in s2:
        asciiVal = ord(letter)
        if charCounts[asciiVal] <= 0:
            return False
        charCounts[ord(letter)]-=1
    
    return True

# print(isPermutation("ABCC", "BACC"))


