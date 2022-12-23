
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

# Write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient
# space at the end to hold the additional characters, and that you given the "true" length of the string.

def urlify(s, length):
    s1 = length * [0]
    for i in range(length):
        asciiVal = ord(s[i])
        if asciiVal == 32:
            s1[i] = "%20"
        else:
            s1[i] = s[i]

    return "".join(s1)

# print(urlify("Mr John Smith    ", 13))
            


