
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

# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or a phrase that is the same forwards and backwards. A permutation is a 
# rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# You can ignore casing and non-letter characters

def isPalindromePermutation(s):
    charCount = 128 * [0]
    oddCount = 0
    for l in s:
        asciiVal = ord(l.lower())
        if 65 <= asciiVal <= 90 or 97 <= asciiVal <= 122:
            charCount[asciiVal]+=1
    for val in charCount:
        if val % 2 != 0:
            oddCount+=1
            if oddCount > 1:
                return False
    return True

# print(isPalindromePermutation("kayak!"))

# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def oneAway(s1, s2):
    modCount = 0
    charArr = 128 * [0]
    for letter in s2:
        aVal = ord(letter)
        charArr[aVal]+=1
    for letter in s1:
        aVal = ord(letter)
        if charArr[aVal] < 1:
            modCount+=1
            if modCount > 1:
                return False
    return True

print(oneAway("pale", "bae"))


            


