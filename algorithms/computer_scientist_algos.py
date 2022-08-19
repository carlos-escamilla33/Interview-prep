#-----------The Self Taught Computer Scientist Algorithm Exercises-----------

# Print the numbers from 1 to 10 recursively
def num_counter(start, end):
    if start > end:
        return
    print(start)
    return num_counter(start + 1, end)

# num_counter(1, 10)

# Given a list of words in alphabetical order, write a function that performs
# binary search for a word and returns whether it is in the list
import math

def findWord(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = math.floor((r + l) / 2)

        if arr[mid] == target:
            return f'Word is in index: {mid}'
        elif ord(arr[mid][0]) < ord(target[0]):
            l+=1
        else:
            r-=1

    print("Word not array")

# print(findWord(["apple", "bee", "caramel", "daisy", "flower"], "flower"))