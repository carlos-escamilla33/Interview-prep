
# ----------------Leetcode #20 Valid Parentheses ---------------- #

def isValid(string):
    bracePairs = {
        "]": "[", 
        ")": "(",
        "}": "{",
    }
    stack = []

    for char in string:
        if char in bracePairs and len(stack) > 0:
            if bracePairs[char] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0