
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

print(isUnique("adf"))


